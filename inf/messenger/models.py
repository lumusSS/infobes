from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    users = models.ManyToManyField(User, related_name="users")
    encrypt_algorithm = models.CharField(max_length=200, null=False, blank=True)
    
    def __str__(self):
        return self.name
    

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_message', on_delete=models.CASCADE, null=False, blank=True, default=1)
    user = models.ForeignKey(User, related_name='user_message', on_delete=models.CASCADE, null=False, blank=False, default=1)
    text_message = models.TextField()
    
    def __str__(self):
        return self.chat.__str__() + " | " + self.user.__str__()
    
    
class RSAKey(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_rsa', on_delete=models.CASCADE, null=False, blank=True)
    
    n = models.TextField()
    
    public_key = models.TextField()
    private_key = models.TextField()
    
    def __str__(self):
        return self.chat.__str__()
    
class RSAOutputKey(models.Model):
    user = models.ForeignKey(User, related_name='user_rsa', on_delete=models.CASCADE, null=False, blank=True)
    
    n = models.TextField()
    
    public_key = models.TextField()
    
    def __str__(self):
        return self.n.__str__()

    
