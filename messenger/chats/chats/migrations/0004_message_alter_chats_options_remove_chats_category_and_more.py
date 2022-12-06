# Generated by Django 4.1.2 on 2022-11-29 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0003_auto_20221124_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст сообщения')),
                ('is_readen', models.BooleanField(default=False, verbose_name='Сообщение прочитано')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_messages', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AlterModelOptions(
            name='chats',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.RemoveField(
            model_name='chats',
            name='category',
        ),
        migrations.RemoveField(
            model_name='chats',
            name='chat_name',
        ),
        migrations.AddField(
            model_name='chats',
            name='title',
            field=models.CharField(max_length=64, null=True, verbose_name='Имя чата'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_messages', to='chats.chats', verbose_name='Принадлежит чату'),
        ),
    ]