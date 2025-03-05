from django.contrib import admin

from . import models

@admin.register(models.RSAKey)
class RSAKeyAdmin(admin.ModelAdmin):
    list_display = ['chat']
    
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['chat']
    
@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['name']
