from messenger.encrypt.encrypt import Encrypt

from channels.db import database_sync_to_async

from django.contrib.auth import get_user_model

from messenger import models

User = get_user_model()

@database_sync_to_async
def _get_user(user_id):
    return User.objects.get(pk=user_id)

@database_sync_to_async
def _get_chat(chat_id):
    return models.Chat.objects.get(pk=chat_id)

@database_sync_to_async
def _get_rsa_key(chat):
    return models.RSAKey.objects.get(chat=chat)

@database_sync_to_async
def _get_output_rsa_key(user):
    return models.RSAOutputKey.objects.get(user=user)

@database_sync_to_async
def _get_output_rsa_keys(user):
    return models.RSAOutputKey.objects.filter(user=user)

@database_sync_to_async
def _create_output_rsa_keys(user, n, public_key):
    models.RSAOutputKey.objects.create(user=user, n=n, public_key=public_key)
    
    
@database_sync_to_async
def _delete_output_rsa_keys(keys):
    keys.delete()
    
@database_sync_to_async
def _is_exists(queryset):
    return queryset.exists()

class RsaEncrypt(Encrypt):
    
    async def initialize(self, query_params):
        
        user_id = query_params.get('user_id', [None])[0]
        
        n = query_params.get('n', [None])[0]
        public_key = query_params.get('public_key', [None])[0]
             
        user = await _get_user(user_id)
        
        keys = await _get_output_rsa_keys(user)
        
        if _is_exists(keys):
            await _delete_output_rsa_keys(keys)

            
        await _create_output_rsa_keys(user, n, public_key)
        
        
    
    async def encrypt(self, encrypt_data):
        
        user_id = encrypt_data['recipients_user_id']
        message = encrypt_data['message']
        
        user = await _get_user(user_id)
        rsa = await _get_output_rsa_key(user)
        
        cipher = [pow(ord(char), int(rsa.public_key), int(rsa.n)) for char in message]
        return cipher
     
    
    async def decrypt(self, decrypt_data):
        
        chat_id = decrypt_data['target_chat']
        message = decrypt_data['message']
        
        chat = await _get_chat(chat_id)
        
        rsa = await _get_rsa_key(chat)
        
        print(type(message))
        
        plain = [chr(pow(int(char), int(rsa.private_key), int(rsa.n))) for char in message]
        return ''.join(plain)
    
