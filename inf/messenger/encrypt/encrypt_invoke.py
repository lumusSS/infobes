
from .encryption_algorithms import encryptions

class EncryptInvoke:
    def __init__(self, encrypt_method):
        self.method = encryptions.get(encrypt_method)
        
    def initialize(self, data):
        encrypt_create_context = self.method['encrypt_context_creator']
        encrypt_create_context.create_context_at_connect(data)
        
    
    