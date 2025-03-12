from abc import ABC, abstractmethod



class Encrypt(ABC):
    
    @abstractmethod
    async def initialize(self, query_params):
        pass
    
    @abstractmethod
    async def encrypt(self, encrypt_context):
        pass
    
    @abstractmethod
    async def decrypt(self, decrypt_context):
        pass
    

def method(encrypt : Encrypt):
    return {"encrypt" : encrypt}
