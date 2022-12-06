from django.db import models
from application import settings

class Chats(models.Model):
    title = models.CharField(max_length=64, null= True, verbose_name='Имя чата')
    description = models.TextField(verbose_name='Описание')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    text = models.TextField(max_length=1024, verbose_name='Текст сообщения')
    is_readen = models.BooleanField(
        default=False, verbose_name='Сообщение прочитано')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        related_name='author_messages'
    )
    chat = models.ForeignKey(
        Chats,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Принадлежит чату',
        related_name='chat_messages'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'