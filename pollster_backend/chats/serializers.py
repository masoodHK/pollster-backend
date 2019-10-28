from django.contrib.auth import get_user_model
from rest_framework import serializers
from userprofile.serializers import UserProfileSerializer

from .models import ChatRoom, Messages

class ChatRoomSerializer(serializers.ModelSerializer):
    users_id = serializers.PrimaryKeyRelatedField(many=True, read_only=False, source='users', queryset=get_user_model().objects.all())
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    sent_by = serializers.ReadOnlyField(source='sent_by.username')
    user_profile_pic = serializers.CharField(source='sent_by.profile_pic_url')
    chat = serializers.PrimaryKeyRelatedField(queryset=ChatRoom.objects.all())
    class Meta:
        model = Messages
        fields = '__all__'