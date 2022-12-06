from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Chat, Message
from users.models import User
from .serializers import ChatSerializer, MessageSerializer
from users.serializers import UserSerializer


class ChatsAPIView(APIView):
    def get(self, request):
        qs = Chat.objects.all()
        return Response({'get' : ChatSerializer(qs, many=True).data})

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'not allowed'})  
        try:
            instance = Chat.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})    
        serializer = ChatSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'delete not allowed'})

        try:
            instance = Message.objects.get(pk=pk)

        except:
            return Response({'error': 'object does not exist'})
        
        Message.objects.get(pk=pk).delete()
        return Response({'delete': True})

class MessagesAPIView(APIView):
    def get(self, request):
        qs = Message.objects.all()
        return Response({'get' : MessageSerializer(qs, many=True).data})

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'put not allowed'})

        try:
            instance = Message.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})

        serializer = MessageSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})

    # curl -X DELETE 'http://127.0.0.1:8000/api/v1/chats/messages/5/' -H 'Content-Type: application/json'
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'delete not allowed'})

        try:
            instance = Message.objects.get(pk=pk)
        except:
            return Response({'error': 'object does not exist'})

        Message.objects.get(pk=pk).delete()
        return Response({'delete': True})