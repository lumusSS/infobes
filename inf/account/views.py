from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import permissions
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import APIException

from djoser.views import TokenCreateView

from djoser import signals, utils
from djoser.conf import settings as settings_djoser

from . import serializers


class LoginAPIView(TokenCreateView):
    permission_classes = [AllowAny]
    
    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings_djoser.SERIALIZERS.token
        
        data = token_serializer_class(token).data
        
        data['user_id'] = serializer.user.id
        
        return Response(
            data=data, status=status.HTTP_200_OK
        )
        
class UserRegistrationAPIView(CreateAPIView):
    
    permission_classes = [AllowAny]
     
    serializer_class = serializers.UserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
    
        try:
            response = super().create(request, *args, **kwargs)
            
            message = {
                "telephone" : True,
                "password" : True,
            }
            
            
            response.data = message
        except APIException as e:
            response = Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        
        return response
