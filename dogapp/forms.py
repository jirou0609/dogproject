from .models import UserAnswer
from django.forms import ModelForm, RadioSelect


class UserAnswerForm(ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5', 'answer_6']
        widgets = {
            'answer_1': RadioSelect,
            'answer_2': RadioSelect,
            'answer_3': RadioSelect,
            'answer_4': RadioSelect,
            'answer_5': RadioSelect,
            'answer_6': RadioSelect,
        }