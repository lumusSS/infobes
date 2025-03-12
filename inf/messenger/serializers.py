from rest_framework import serializers 
from rest_framework.exceptions import APIException

from . import models

class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RSAKey
        fields = ['public_key', 'n']
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = ['name', 'encrypt_algorithm']