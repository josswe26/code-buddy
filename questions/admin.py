from django.contrib import admin
from .models import Question, Reply
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on', 'last_updated')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'last_updated')
    search_fields = ('title', 'content', 'author__username')

    summernote_fields = ('content')


@admin.register(Reply)
class ReplyAdmin(SummernoteModelAdmin):

    list_display = ('body', 'author', 'created_on', 'last_updated')
    list_filter = ('created_on', 'last_updated')
    search_fields = ('body', 'author__username')

    summernote_fields = ('body')
