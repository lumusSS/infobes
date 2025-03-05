
from encrypt_context_creator import EncryptContextCreator

class RsaEncryptContextCreator(EncryptContextCreator):
    
    def create_context_at_connect(self, data):
        pass
    
    def create_encrypt_context(self, context):
        e_context = {}
        
        e_context['public_key'] = context.get('public_key')
        e_context['n'] = context.get('n')
        
        return e_context
    
    def create_decrypt_context(self, context):
        d_context = {}
        
        d_context['private_key'] = context.get('private_key')
        d_context['n'] = context.get('n')
        
        return d_context