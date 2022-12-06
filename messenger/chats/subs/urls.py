from django.urls import path
from subs.views import subs

urlpatterns = [
    path('', subs , name='dialogs'),
]