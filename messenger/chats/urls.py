from django.urls import path
from chats.views import get_all_chats, get_chat, update_chat, create_chat, delete_chat
from chats.views import get_message, update_message, get_all_messages, create_message
from chats.views import delete_message, add_member, delete_message, read_message, delete_member


urlpatterns = [
    path('get_chat/', get_chat, name='get_chat'),
    path('get_message/', get_message, name='get_message'),
    path('update_chat/', update_chat, name='update_chat'),
    path('update_message/', update_message, name='update_message'),
    path('get_all_chats/', get_all_chats, name='get_all_chats'),
    path('get_all_messages/', get_all_messages, name='get_all_messages'),
    path('create_chat/', create_chat, name='create_chat'),
    path('delete_chat/', delete_chat, name='delete_chat'),
    path('create_message/', create_message, name='create_message'),
    path('delete_message/', delete_message, name='delete_message'),
    path('add_member/', add_member, name='add_member'),
    path('delete_member/', delete_member, name='delete_member'),
    path('read_message/', read_message, name='read_message')
]