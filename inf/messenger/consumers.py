import json
from djangochannelsrestframework.consumers import AsyncJsonWebsocketConsumer

from channels.db import database_sync_to_async

from urllib.parse import parse_qs

from .chat.chat_info import ChatInfo

from .encrypt import encrypt_invoker

from . import models


@database_sync_to_async
def create_message(target_chat_id, user_id, message):
    
    chat = models.Chat.objects.get(pk=target_chat_id)
    user = models.User.objects.get(pk=user_id)
    models.Message.objects.create(user=user, chat=chat, text_message=message)

class ChatConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        
        self.user = self.scope['user']
            
        if not self.user.is_authenticated:
            await self.close()
            
        query_params = parse_qs(self.scope['query_string'].decode())
            
        chat_info = ChatInfo(self.user, query_params)
        self.chat_id = chat_info.get_chat_id()
        self.chat_name = chat_info.get_name()
        
        await encrypt_invoker.singleton.initialize(query_params, self.chat_id)
            
        await self.channel_layer.group_add(
            self.chat_name,
            self.channel_name
        )
            
        await self.accept()

            
    
    async def disconnect(self, code):
        if self.user.is_authenticated: 
            await self.channel_layer.group_discard(
                    self.chat_name,
                    self.channel_name
                )
            
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        
        user_id = data.get('user_id')
        target_chat_id = data.get('target_chat')
        message = data.get('message')
        
        if target_chat_id and message:
            
            message = await encrypt_invoker.singleton.decrypt(data, target_chat_id)
            
            data['message'] = message
        
            await create_message(target_chat_id, user_id, message)
        
            await self.channel_layer.group_send(
                f"chat_{target_chat_id}",
                {
                    'type' : 'chat.message',
                    'data' : data,
                    'message' : message,
                }
            )
            
            
    async def chat_message(self, event):
        
        user = self.scope['user']
        message = event.get('message')
        
        data = event.get('data')
        
        target_chat_id = data.get('target_chat')
        
        data['recipients_user_id'] = user.id
        data['message'] = message
        
        message = await encrypt_invoker.singleton.encrypt(data, target_chat_id)
        
        await self.send(text_data=json.dumps({
            "chat_id" : self.chat_id,
            "message" : message,
        }))