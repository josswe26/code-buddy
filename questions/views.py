from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.postgres.search import SearchVector
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.db.models import Sum
from .models import Question, Reply, QuestionVote, ReplyVote
from .forms import QuestionForm, ReplyForm


class QuestionListView(generic.ListView):
    """ List view to render all questions """

    model = Question
    paginate_by = 10

    queryset = Question.objects.all().order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """ Get question list and question form and return data for rendering"""
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['question_form'] = QuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        """ Post method for QuestionForm """
        question_form = QuestionForm(data=request.POST)

        if question_form.is_valid():
            question_form.instance.author = request.user
            question_form.instance.slug = slugify(question_form.instance.title)
            question_form.save()
            messages.add_message(request, messages.SUCCESS,'Your question has been submitted successfully. Thank for your collaboration!')
        else:
            question_form = QuestionForm()
            messages.add_message(request, messages.ERROR,'There was an error submitting your question. Please try again!')

        return HttpResponseRedirect(reverse('home'))
        

class QuestionDetailView(View):
    """  View to render detailed information of a specific question """

    def get(self, request, slug, *args, **kwargs):
        """ Get question information and return data for rendering """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, slug=slug)
        replies = question.replies.all().order_by('-votes_score')
        
        return render(
            request,
            'question_detail.html',
            {
                'question': question,
                'replies': replies,
                'reply_form': ReplyForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """ Post method for ReplyForm """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, slug=slug)

        reply_form = ReplyForm(data=request.POST)

        if reply_form.is_valid():
            reply_form.instance.author = request.user
            reply = reply_form.save(commit=False)
            reply.question = question
            reply_form.save()
            messages.add_message(request, messages.SUCCESS,'Your reply has been submitted successfully. Thank for your collaboration!')
        else:
            reply_form = ReplyForm()
            messages.add_message(request, messages.ERROR,'There was an error submitting your reply. Please try again!')

        return HttpResponseRedirect(reverse('question_detail', args=[slug]))


class QuestionEditView(View):
    """ View to edit a specific question"""

    def get(self, request, id, *args, **kwargs):
        """ Get question information and return form to edit """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, id=id)

        data = {'title': question.title, 'content': question.content}
        edit_form = QuestionForm(initial=data)

        return render(
            request,
            'edit_question.html',
            {
                'question': question,
                'edit_form': edit_form
            }
        )

    def post(self, request, id, *args, **kwargs):
        """ Update question information """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, id=id)

        edit_form = QuestionForm(instance=question, data=request.POST)

        if edit_form.is_valid():
            question.title = edit_form.cleaned_data.get('title')
            question.content = edit_form.cleaned_data.get('content')
            question.slug = slugify(edit_form.cleaned_data.get('title'))
            question.save()
            messages.add_message(request, messages.SUCCESS,'You edited your question successfully.')
        else:
            edit_form = QuestionForm()
            messages.add_message(request, messages.WARNING,'Your question has not been edited.')

        return HttpResponseRedirect(reverse('home'))


class QuestionDeleteView(View):
    """ View to delete a specific question"""

    def get(self, request, id, *args, **kwargs):
        """ Get question information and return form to delete """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, id=id)

        return render(
            request,
            'delete_question.html',
            {
                'question': question,
            }
        )

    def post(self, request, id, *args, **kwargs):
        """ Delete question """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, id=id)

        question.delete()
        messages.add_message(request, messages.SUCCESS,'Your question has been deleted.')

        return HttpResponseRedirect(reverse('home'))


class ReplyEditView(View):
    """ View to edit a specific reply"""

    def get(self, request, id, *args, **kwargs):
        """ Get reply information and return form to edit """
        queryset = Reply.objects.all()
        reply = get_object_or_404(queryset, id=id)

        data = {'body': reply.body}
        edit_form = ReplyForm(initial=data)

        return render(
            request,
            'edit_reply.html',
            {
                'reply': reply,
                'edit_form': edit_form
            }
        )

    def post(self, request, id, *args, **kwargs):
        """ Update reply information """
        queryset = Reply.objects.all()
        reply = get_object_or_404(queryset, id=id)

        edit_form = ReplyForm(instance=reply, data=request.POST)

        if edit_form.is_valid():
            reply.body = edit_form.cleaned_data.get('body')
            reply.save()
            messages.add_message(request, messages.SUCCESS,'You edited your reply successfully.')
        else:
            edit_form = ReplyForm()
            messages.add_message(request, messages.WARNING,'Your reply has not been edited.')

        return HttpResponseRedirect(reverse('question_detail', args=[reply.question.slug]))


class ReplyDeleteView(View):
    """ View to delete a specific reply"""

    def get(self, request, id, *args, **kwargs):
        """ Get reply information and return form to delete """
        queryset = Reply.objects.all()
        reply = get_object_or_404(queryset, id=id)
        question_slug = reply.question.slug

        return render(
            request,
            'delete_reply.html',
            {
                'reply': reply,
            }
        )

    def post(self, request, id, *args, **kwargs):
        """ Delete reply """
        queryset = Reply.objects.all()
        reply = get_object_or_404(queryset, id=id)
        slug = reply.question.slug

        reply.delete()
        messages.add_message(request, messages.SUCCESS,'Your reply has been deleted.')

        return HttpResponseRedirect(reverse('question_detail', args=[slug]))


class SearchListView(View):
    """ List view for questions matching a search """

    def post(self, request):
        """ Search questions matching the search """
       
        searched = request.POST['searched']
        questions = Question.objects.annotate(
            search=SearchVector('title', 'content')).filter(search=searched)

        return render(request,
        'search_results.html',
        {'searched': searched,
        'questions': questions}
        )


class VoteQuestion(View):
    """ Vote Queston view """

    def post(self, request, id):
        """ Register question votes """

        vote = QuestionVote()
        question = get_object_or_404(Question, id=id)

        score = request.POST.get('vote_score')

        existing_vote = QuestionVote.objects.filter(voter=request.user, score=score, question=question)

        if existing_vote:
            existing_vote.delete()

            question.upvoted = False
            question.downvoted = False

        else:
            vote, created = QuestionVote.objects.update_or_create(
                voter=request.user,
                question=question,
                defaults={'score': score},
            )

            if vote.score == '1':
                question.upvoted = True
                question.downvoted = False
            elif vote.score == '-1':
                question.downvoted = True
                question.upvoted = False

            vote.save()
            
        try:
            total_score = QuestionVote.objects.filter(question=question).aggregate(Sum('score'))
            question.votes_score = total_score['score__sum']
            question.save()
        except:
            question.votes_score = 0
            question.save()

        if request.POST.get('location') == 'home':
            return HttpResponseRedirect(reverse('home'))

        if request.POST.get('location') == 'question_detail':
            return HttpResponseRedirect(reverse('question_detail', args=[question.slug]))


class VoteReply(View):
    """ Vote Reply view """

    def post(self, request, id):
        """ Register reply votes """

        vote = ReplyVote()
        reply = get_object_or_404(Reply, id=id)

        score = request.POST.get('vote_score')

        existing_vote = ReplyVote.objects.filter(voter=request.user, score=score, reply=reply)

        if existing_vote:
            existing_vote.delete()

            reply.upvoted = False
            reply.downvoted = False
        else:
            vote, created = ReplyVote.objects.update_or_create(
                voter=request.user,
                reply=reply,
                defaults={'score': score},
            )

            if score == '1':
                reply.upvoted = True
                reply.downvoted = False
            elif score == '-1':
                reply.downvoted = True
                reply.upvoted = False
                
            vote.save()

        try:
            total_score = ReplyVote.objects.filter(reply=reply).aggregate(Sum('score'))
            reply.votes_score = total_score['score__sum']
            reply.save()
        except:
            reply.votes_score = 0
            reply.save()

        return HttpResponseRedirect(reverse('question_detail', args=[reply.question.slug]))
        