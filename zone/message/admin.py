from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date')
    list_display_links = ('id','name')

admin.site.register(Message, MessageAdmin)