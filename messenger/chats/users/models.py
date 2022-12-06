from django.db import models
from django.contrib.auth.models import AbstractUser
from chats.models import Chats

class User(AbstractUser):
    #username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField('Email', max_length=256, blank=True)
    about = models.TextField('О себе', max_length=1024, blank=True)
    chat = models.ManyToManyField(
        Chats,
        blank=True,
        verbose_name='Чаты',
    )