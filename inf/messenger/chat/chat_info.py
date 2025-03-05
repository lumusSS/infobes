from .web_socket_group_info import GroupInfo

class ChatInfo(GroupInfo):
    
    def __init__(self, user, query):
        self.user = user
        self.query = query
    
    def get_chat_id(self):
        chat_id = self.query.get('chat_id', [None])[0]
        return chat_id
    
    def get_name(self):
        
        chat_id = self.get_chat_id()
        
        return f"chat_{chat_id}"