from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'dogapp'

class IndexView(TemplateView):
    template_name = 'index.html'