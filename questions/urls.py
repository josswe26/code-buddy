from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('<slug:slug>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('ask_question', views.AskQuestionView.as_view(), name='ask_question'),
    path('new_reply/<int:question_id>/', views.NewReplyView.as_view(), name='new_reply'),
    path('edit_question/<int:id>/', views.QuestionEditView.as_view(), name='edit_question'),
    path('delete_question/<int:id>/', views.QuestionDeleteView.as_view(), name='delete_question'),
    path('edit_reply/<int:id>/', views.ReplyEditView.as_view(), name='edit_reply'),
    path('delete_reply/<int:id>/', views.ReplyDeleteView.as_view(), name='delete_reply'),
    path('search_results', views.SearchListView.as_view(), name='search_results'),
    path('vote_question/<int:id>', views.VoteQuestion.as_view(), name='vote_question'),
    path('vote_reply/<int:id>', views.VoteReply.as_view(), name='vote_reply'),
    path('about', TemplateView.as_view(template_name="about.html"), name='about'),
    path('404', TemplateView.as_view(template_name="404.html"), name='404'),
    ]
