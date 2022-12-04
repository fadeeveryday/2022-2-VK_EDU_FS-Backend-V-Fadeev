from django.urls import path
from chats.views import get_all_chats, get_chat, update_chat, create_chat, delete_chat


urlpatterns = [
    path('get_chat/', get_chat, name='get_chat'),
    path('update_chat/', update_chat, name='update_chat'),
    path('get_all_chats/', get_all_chats, name='get_all_chats'),
    path('create_chat/', create_chat, name='create_chat'),
    path('delete_chat/', delete_chat, name='delete_chat'),
]