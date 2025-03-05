from encrypt import Encrypt

class RsaEncrypt(Encrypt):
    def encrypt(self, encrypt_context):
        
        public_key = encrypt_context.get('public_key')
        n = encrypt_context.get('n')
        message = encrypt_context.get('message')
        
        cipher = [pow(ord(char), public_key, n) for char in message]
        return cipher
     
    
    def decrypt(self, decrypt_context):
        
        private_key = decrypt_context.get('private_key')
        n = decrypt_context.get('n')
        message = decrypt_context.get('message')
        
        plain = [chr(pow(char, private_key, n)) for char in message]
        return ''.join(plain)
    
