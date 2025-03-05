from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

@database_sync_to_async
def get_user_from_token(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()
    
    

class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        instance = TokenAuthMiddlewareInstance(scope, self)
        await instance(receive, send)
        
        

class TokenAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.scope = dict(scope)
        self.inner = middleware.inner

    async def __call__(self, receive, send):
        token_key = None

        query_string = self.scope.get('query_string', b'').decode()
        qs = parse_qs(query_string)
        token_key = qs.get('token', [None])[0]

        if token_key is None:
            headers = dict((k.decode(), v.decode()) for k, v in self.scope.get('headers', []))
            auth_header = headers.get('authorization')
            if auth_header:
                parts = auth_header.split()
                if len(parts) == 2 and parts[0].lower() == 'token':
                    token_key = parts[1]

        self.scope['user'] = await get_user_from_token(token_key) if token_key else AnonymousUser()

        await self.inner(self.scope, receive, send)