from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from . import models, serializers

from .rsa.RsaAlgorithm import RSA

class SendingPublicKeyAPI(APIView):
    def get(self, request, chat_id):
        chat = models.Chat.objects.get(pk=chat_id)
        rsa_keys = models.RSAKey.objects.filter(chat=chat)
        rsa_key = None
        
        if not rsa_keys.exists():
            
            rsa = RSA()
            
            n = rsa.p * rsa.q
            
            public_key = rsa.public_key
            private_key = rsa.private_key
            
            rsa_key = models.RSAKey.objects.create(
                chat=chat, 
                public_key=public_key, 
                private_key=private_key, 
                n=n
            )
            
        else:
            rsa_key = rsa_keys[0]
            
        public_key_serializer = serializers.PublicKeySerializer(rsa_key)
        
        data_response = public_key_serializer.data
        
        return Response(data_response)
