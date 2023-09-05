from django.contrib import admin
from .models import Dogs


class DogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'dog_name')
    list_display_links = ('id', 'dog_name')

admin.site.register(Dogs, DogsAdmin)