from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('send_public_key/<int:user_id>', views.SendingPublicKeyAPI.as_view(), name='general'),
    path('get_chats_for_user/<int:user_id>', views.GetChatsForUser.as_view(), name='get-chats-for_user'),
]
