
from abc import ABC, abstractmethod

class EncryptContextCreator(ABC):
    
    @abstractmethod
    def create_context_at_connect(self, data):
        pass
    
    @abstractmethod
    def create_encrypt_context(self, context):
        pass
    
    @abstractmethod
    def create_decrypt_context(self, context):
        pass
    
    @abstractmethod
    def create_response(self, context):
        pass
    
