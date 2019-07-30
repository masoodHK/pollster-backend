from rest_framework import serializers

from .models import Poll, Option, Comments
from categories.models import Categories

class PollsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())
    class Meta:
        model = Poll
        fields = (
            'id', 
            'question', 
            'date_created', 
            'date_updated', 
            'poll_type',
            'is_active',
            'ends_on',
            'category'
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
    class Meta:
        model = Comments
        fields = (
            'id',
            'poll',
            'comment_text',
            'date_created', 
            'date_updated', 
        )
        read_only_fields = ['id']