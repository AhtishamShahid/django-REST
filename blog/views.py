from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from blog.models import Post, Category
from blog.serializers import PostSerializer, CategorySerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
