from rest_framework import serializers 


from django.contrib.auth import get_user_model, authenticate

from rest_framework.exceptions import APIException

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True) 
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['telephone', 'first_name', 'last_name', 'password', 'password2']
        
    def create(self, validated_data):
        
        user = get_user_model().objects.create(
            username=validated_data['telephone'],
            telephone=validated_data['telephone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        
        user.set_password(validated_data['password'])
        
        user.save()
        
        return user
        
    def validate(self, data):
        
        telephone = data['telephone']
        password1 = data['password']
        password_re = data['password2']
        
        error = False
        error_message = {
            "telephone" : True,
            "password" : True,
        }
        
        if get_user_model().objects.filter(telephone=telephone).exists():
            error_message['telephone'] = False
            error = True
        
        if password1 != password_re:
            error_message['password'] = False
            error = True
            
        if error:
            raise APIException(error_message)
        
        return data