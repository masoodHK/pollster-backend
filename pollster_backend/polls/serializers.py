from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Poll, Option, Comments
from categories.models import Categories

class PollsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())
    created_by = serializers.ReadOnlyField(source="created_by.username")
    profile_pic = serializers.CharField(source='created_by.profile_pic_url')
    class Meta:
        model = Poll
        fields = (
            'id', 
            'question', 
            'date_created', 
            'date_updated',
            'created_by', 
            'poll_type',
            'is_active',
            'ends_on',
            'category',
            'profile_pic'
        )
        read_only_fields = ['id']

class OptionsSerializer(serializers.ModelSerializer):
    poll = serializers.PrimaryKeyRelatedField(queryset=Poll.objects.all())
    class Meta:
        model = Option
        fields = (
            'id',
            'poll',
            'votes',
            'option_text'
        )
        read_only_fields = ['id']

class CommentsSerializer(serializers.ModelSerializer):
    poll = serializers.PrimaryKeyRelatedField(queryset=Poll.objects.all())
    made_by = serializers.ReadOnlyField(source="made_by.username")
    profile_pic = serializers.CharField(source='made_by.profile_pic_url')
    class Meta:
        model = Comments
        fields = (
            'id',
            'poll',
            'comment_text',
            'date_created',
            'made_by', 
            'date_updated',
            'profile_pic' 
        )
        read_only_fields = ['id', 'made_by', 'profile_pic']