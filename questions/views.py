from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Question
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
            question_form.instance.author_id = request.user.id
            question_form.instance.slug = slugify(question_form.instance.title)
            question_form.save()
        else:
            question_form = QuestionForm()

        return HttpResponseRedirect(reverse('home'))


class QuestionDetailView(View):
    """  View to render detailed information of a specific question """

    def get(self, request, slug, *args, **kwargs):
        """ Get question information and return data for rendering """
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, slug=slug)
        replies = question.replies.all().order_by('created_on')
        
        return render(
            request,
            'question_detail.html',
            {
                'question': question,
                'replies': replies,
                'reply_form': ReplyForm()
            }
        )
