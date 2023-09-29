from .models import Comment, ReplyComment
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


class ReplyCommentForm(forms.Form):
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label='返信コメント'
    )
    parent_comment_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )