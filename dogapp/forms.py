from .models import UserAnswer
from django.forms import ModelForm
from django import forms


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5', 'answer_6']


# class UserAnswerForm(forms.Form):
#     form_answer_1 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])
#     form_answer_2 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])
#     form_answer_3 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])
#     form_answer_4 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])
#     form_answer_5 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])
#     form_answer_6 = forms.ChoiceField(choices=[('1', '回答１'), ('2', '回答２'), ('3', '回答３')])