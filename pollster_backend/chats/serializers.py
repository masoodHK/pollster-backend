from rest_framework import serializers
from userprofile.serializers import UserProfileSerializer

from .models import ChatRoom, Messages

class ChatRoomSerializer(serializers.ModelSerializer):
    users = UserProfileSerializer(many=True)
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    sent_by = serializers.ReadOnlyField(source='sent_by.username')
    chat = serializers.PrimaryKeyRelatedField(queryset=ChatRoom.objects.all())
    class Meta:
        model = Messages
        fields = '__all__'