from . import views
from django.urls import path


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='home'),
    path('<slug:slug>/', views.QuestionDetailView.as_view(), name='question_detail')
]
