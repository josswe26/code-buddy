from django.contrib import admin
from .models import Question, Reply


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on', 'last_updated')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'last_updated')
    search_fields = ('title', 'content', 'author__username')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):

    list_display = ('body', 'author', 'created_on', 'last_updated')
    list_filter = ('created_on', 'last_updated')
    search_fields = ('body', 'author__username')
