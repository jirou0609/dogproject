from .models import UserAnswer
from django.forms import ModelForm
from django import forms


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5', 'answer_6']

