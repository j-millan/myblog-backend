from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogPost, BlogComment
from blog.serializers import BlogPostSerializer, BlogCommentSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
