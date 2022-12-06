from django.urls import path
from chats.views import (
    ChatsAPIList,
    MessagesAPIList,
    ChatsAPIDetailView,
    MessagesAPIDetailView,
    DeleteMemberFromChat,
)

urlpatterns = [
    path('messages/<int:chat_id>/', MessagesAPIList.as_view()),
    path('user_chats/<int:user_id>/', ChatsAPIList.as_view()),
    path('chat/<int:pk>/', ChatsAPIDetailView.as_view()),
    path('message/<int:pk>/', MessagesAPIDetailView.as_view()),
    path('chat/delete_member/', DeleteMemberFromChat.as_view()),
]

# urlpatterns = [
#     path('get_chat/', get_chat, name='get_chat'),
#     path('get_message/', get_message, name='get_message'),
#     path('update_chat/', update_chat, name='update_chat'),
#     path('update_message/', update_message, name='update_message'),
#     path('get_all_chats/', get_all_chats, name='get_all_chats'),
#     path('get_all_messages/', get_all_messages, name='get_all_messages'),
#     path('create_chat/', create_chat, name='create_chat'),
#     path('delete_chat/', delete_chat, name='delete_chat'),
#     path('create_message/', create_message, name='create_message'),
#     path('delete_message/', delete_message, name='delete_message'),
#
#     path('add_member/', add_member, name='add_member'),
#     path('delete_member/', delete_member, name='delete_member'),
#     path('read_message/', read_message, name='read_message')
# ]