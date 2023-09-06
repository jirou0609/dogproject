from django.contrib import admin
from django.urls import path
from .import views
app_name = 'dogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('choiceform/', views.CreateAnswerView.as_view(), name='choiceform'),
]
