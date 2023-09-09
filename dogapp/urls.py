from django.contrib import admin
from django.urls import path
from .import views

app_name = 'dogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('question1/', views.question1, name='question1'),
    path('question2/', views.question2, name='question2'),
    path('question3/', views.question3, name='question3'),
    path('question4/', views.question4, name='question4'),
    path('question5/', views.question5, name='question5'),
    path('question6/', views.question6, name='question6'),
    path('create_answer/', views.create_answer, name='create_answer'),
]
