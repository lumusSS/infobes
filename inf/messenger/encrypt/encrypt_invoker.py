
from .encryption_algorithms import encryptions

from channels.db import database_sync_to_async, sync_to_async

from messenger import models

@database_sync_to_async
def get_chat(chat_id):
    return models.Chat.objects.get(pk=chat_id)



def get_encrypt_method(chat):
    
    encrypt_method = None
    
    if chat:
        algorithm_name = chat.encrypt_algorithm
        encrypt_method = encryptions[algorithm_name]['encrypt']
        
    return encrypt_method

class EncryptInvoker:
    
    def __init__(self):
        pass

        
    async def initialize(self, query_params, chat_id):
        chat = await get_chat(chat_id)
    
        encrypt_method = get_encrypt_method(chat)
        
        await encrypt_method.initialize(query_params)
        
        
    async def encrypt(self, data, chat_id):
        chat = await get_chat(chat_id)
    
        encrypt_method = get_encrypt_method(chat)
        
        response = await encrypt_method.encrypt(data)
        
        return response
        
    async def decrypt(self, data, chat_id):
        chat = await get_chat(chat_id)
    
        encrypt_method = get_encrypt_method(chat)
        
        response = await encrypt_method.decrypt(data)
        
        return response
        
        
singleton = EncryptInvoker()
        
        
        
    
    