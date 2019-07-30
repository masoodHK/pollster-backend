from rest_framework import serializers

from .models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (
            'id',
            'category_name',
            'category_description'
        )
        read_only_fields = ['id']