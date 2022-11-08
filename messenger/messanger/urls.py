from django.urls import path
from messanger.views import message_id

urlpatterns = [
    path('dialogs/<int:message_id>/', message_id , name='dialogs'),
]