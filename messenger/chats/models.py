from django.db import models
from application import settings

class Category (models.Model):
    title = models.CharField(max_length=64, verbose_name='Категории')


class Chats(models.Model):
    chat_name = models.CharField(max_length=64, null=True,  verbose_name='Название чата')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор'
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)