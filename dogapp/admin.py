from django.contrib import admin
from .models import Dogs, UserAnswer, Choice


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