from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Post
from .serializers import *


class PostListAPIViews(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDatailAPIViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer