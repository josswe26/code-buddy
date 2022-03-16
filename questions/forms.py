from .models import Question
from django import forms
from django_summernote.widgets import SummernoteWidget

class QuestionForm(forms.ModelForm):
    """ Form for question submission """
    class Meta:
        model = Question
        fields = ["title", "content"]
        widgets = { 
			'content': SummernoteWidget(),
		}