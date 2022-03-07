from django.shortcuts import render
from django.views.generic import list
from .models import Question


class QuestionListView(ListView):

    model = Question
    paginate_by = 10

    queryset = Question.objects.all().order_by('-created.on')
    template_name = 'index.html'
