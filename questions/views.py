from django.shortcuts import render
from django.views import generic
from .models import Question


class QuestionListView(generic.ListView):

    model = Question
    paginate_by = 10

    queryset = Question.objects.all().order_by('-created_on')
    template_name = 'index.html'
