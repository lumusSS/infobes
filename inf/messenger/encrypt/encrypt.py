from abc import ABC, abstractmethod

from .encrypt_context_creator import EncryptContextCreator

class Encrypt(ABC):
    
    @abstractmethod
    def initialize(self, initialize_context):
        pass
    
    @abstractmethod
    def encrypt(self, encrypt_context):
        pass
    
    @abstractmethod
    def decrypt(self, decrypt_context):
        pass
    

def method(encrypt : Encrypt, encrypt_context_creator : EncryptContextCreator):
    return {"encrypt" : encrypt, "encrypt_context_creator" : encrypt_context_creator}
