from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = [
            'password', 
            'groups', 
            'user_permissions', 
            'is_staff', 
            'is_active', 
            'is_superuser'
        ]

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data.get('username', None),
            email=validated_data.get('email', None)
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
