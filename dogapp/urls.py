from django.contrib import admin
from django.urls import path
from .import views

app_name = 'dogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dog_list/', views.DogsView.as_view(), name='dog_list'),
    path('dog_detail/<int:pk>/', views.DetailView.as_view(), name='dog_detail'),
    path('ranking/', views.count_results, name='ranking'),
    path('dogs/<int:dog_id>/', views.result, name='result'),
    path('question1/', views.question1, name='question1'),
    path('question2/', views.question2, name='question2'),
    path('question3/', views.question3, name='question3'),
    path('question4/', views.question4, name='question4'),
    path('question5/', views.question5, name='question5'),
    path('question6/', views.question6, name='question6'),
    path('create_answer/', views.create_answer, name='create_answer'),
    path('comment/', views.CommentListView.as_view(), name='comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment_detail/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('reply/', views.reply_to_comment, name='reply'),
]
