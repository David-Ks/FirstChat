from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MyChat.as_view(), name='chat'),
    path('msender/', MailSender.as_view(), name='msender'),
]