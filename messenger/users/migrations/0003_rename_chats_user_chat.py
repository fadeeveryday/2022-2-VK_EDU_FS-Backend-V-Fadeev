# Generated by Django 4.1.2 on 2022-11-21 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_chats_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='chats',
            new_name='chat',
        ),
    ]
