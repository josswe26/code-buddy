from .models import Question, Reply
from django import forms
from django_summernote.widgets import SummernoteWidget

class QuestionForm(forms.ModelForm):
    """ Form for question submission """
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = { 
			'content': SummernoteWidget(),
		}


class ReplyForm(forms.ModelForm):
    """ Form for reply submission """
    class Meta:
        model = Reply
        fields = ['body',]
        widgets = { 
			'body': SummernoteWidget(),
		}