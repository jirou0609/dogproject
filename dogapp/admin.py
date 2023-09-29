from django.contrib import admin
from .models import Dogs, UserAnswer, Choice, Result, Comment, ReplyComment


class DogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'dog_name')
    list_display_links = ('id', 'dog_name')
admin.site.register(Dogs, DogsAdmin)


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
admin.site.register(UserAnswer, UserAnswerAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'dog_name')
    list_display_links = ('id', 'dog_name')
admin.site.register(Choice, ChoiceAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'user')
    list_display_links = ('id', 'result', 'user')
admin.site.register(Result, ResultAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'user')
    list_display_links = ('id', 'category', 'user')
admin.site.register(Comment, CommentAdmin)


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_comment', 'comment_text')
    list_display_links = ('id', 'parent_comment', 'comment_text')
admin.site.register(ReplyComment, ReplyCommentAdmin)