from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UserAnswerForm

app_name = 'dogapp'

class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')
class CreateAnswerView(CreateView):
    form_class = UserAnswerForm
    template_name = 'choiceform.html'
    success_url = reverse_lazy('dogapp:index')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)