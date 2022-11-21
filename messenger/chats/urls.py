from django.urls import path
from chats.views import chat_list, chat_page, chat_create, chat_id


urlpatterns = [
    path('list/', chat_list, name='chat_list'),
    path('page/<int:id>/', chat_page, name='chat_page'),
    path('create/', chat_create, name='chat_create'),
    path('dialogs/<int:message_id>/', chat_id , name='dialogs'),
]