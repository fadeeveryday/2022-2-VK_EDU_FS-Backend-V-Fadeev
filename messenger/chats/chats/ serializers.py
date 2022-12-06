from rest_framework import serializers
from .models import Chats, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ('title', 'description', 'author_id')

    title = serializers.CharField()
    description = serializers.CharField(max_length = 20)
    author_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Chats.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance это объект модели Chat
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    text = serializers.CharField()
    is_readen = serializers.BooleanField(default=False)
    author_id = serializers.IntegerField()
    chat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance это объект модели Chat
        instance.text = validated_data.get('text', instance.text)
        instance.is_readen = validated_data.get('is_readen', instance.is_readen)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.chat_id = validated_data.get('chat_id', instance.chat_id)
        instance.save()
        return instance