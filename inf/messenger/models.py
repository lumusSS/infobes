from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    users = models.ManyToManyField(User, related_name="users")

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_message', on_delete=models.CASCADE, null=False, blank=True, default=1)
    text_message = models.TextField()
    
class RSAKey(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_rsa', on_delete=models.CASCADE, null=False, blank=True)
    
    n = models.TextField()
    
    public_key = models.TextField()
    private_key = models.TextField()
    
    
    #Output key
    
    output_n = models.TextField()
    
    output_public_key = models.TextField()
    output_private_key = models.TextField()
    
