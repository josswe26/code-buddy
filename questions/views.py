from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Question


class QuestionListView(generic.ListView):

    model = Question
    paginate_by = 10

    queryset = Question.objects.all().order_by('-created_on')
    template_name = 'index.html'


class QuestionDetailView(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Question.objects.all()
        question = get_object_or_404(queryset, slug=slug)
        replies = question.replies.all().order_by('created_on')
        
        return render(
            request,
            'question_detail.html',
            {
                'question': question,
                "replies": replies,
            }
        )
