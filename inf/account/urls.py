from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register_user', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login', views.LoginAPIView.as_view(), name='login'),
]
