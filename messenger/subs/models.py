from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User

class Subscribes(models.Model):
    subs_name = models.CharField(max_length=64, verbose_name='Название подписки')
    subs_active = models.BooleanField(verbose_name='Статус подписки')
    subs_time = models.DateTimeField(verbose_name='Дата подписки')
    action = models.DurationField(verbose_name='Оставшееся время')
    users = models.ManyToManyField(
        User,
        blank=True,
        verbose_name='Пользователи',
    )

