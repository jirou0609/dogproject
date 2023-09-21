from .models import Comment
from django.forms import ModelForm
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['category', 'comment_text']
        # categoryフィールドをNULLを許容するためにrequiredをFalseに設定
        widgets = {
            'category': forms.Select(attrs={'required': False}),
        }

