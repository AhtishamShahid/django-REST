from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        depth = 1


class PostSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
        # depth = 1
        category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
