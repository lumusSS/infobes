"""
ASGI config for inf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inf.settings')

django.setup()

import messenger.routing

from messenger.middleware import TokenAuthMiddleware

from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  
    "websocket": TokenAuthMiddleware(
        URLRouter(messenger.routing.websocket_urlpatterns)
    )
})
