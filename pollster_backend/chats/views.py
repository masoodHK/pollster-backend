from django.shortcuts import render

from rest_framework import generics

from .serializers import MessagesSerializer, ChatRoomSerializer
from .models import Messages, ChatRoom

# Create your views here.
class MessagesView(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer
    
    def get_queryset(self):
        return Messages.objects.filter(chat=self.kwargs['chat_id'])

    def perform_create(self, serializer):
        serializer.save(sent_by=self.request.user)

class MessagesRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset

class ChatRoomView(generics.ListCreateAPIView):
    serializer_class = ChatRoomSerializer
    
    def get_queryset(self):
        return ChatRoom.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class ChatRoomRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset