from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'media_type', 'timestamp')
    list_filter = ('media_type', 'timestamp')
