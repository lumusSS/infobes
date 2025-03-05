import json
from djangochannelsrestframework.consumers import AsyncJsonWebsocketConsumer

from urllib.parse import parse_qs

from .chat.chat_info import ChatInfo

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        
        self.user = self.scope['user']
            
        if not self.user.is_authenticated:
            await self.close()
            
        query_params = parse_qs(self.scope['query_string'].decode())
            
        chat_info = ChatInfo(self.user, query_params)
        self.chat_id = chat_info.get_chat_id()
        self.chat_name = chat_info.get_name()
            
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
        
            await self.channel_layer.group_send(
                f"chat_{target_chat_id}",
                {
                    'type' : 'chat.message',
                    'message' : message,
                }
            )
        
            
    async def chat_message(self, event):
        
        message = event['message']
        
        await self.send(text_data=json.dumps({
            "chat_id" : self.chat_id,
            "message" : message,
        }))