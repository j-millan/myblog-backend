from django.shortcuts import get_object_or_404, render

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogPost, BlogComment
from blog.serializers.blog_post import BlogPostSerializer, BlogPostCreateSerializer
from blog.serializers.blog_comment import BlogCommentSerializer, BlogCommentCreateSerializer, BlogCommentUpdateSerializer
from blog.permissions import IsOwnerOrReadOnly

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogPostCreateSerializer
        else:
            return BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogPostSerializer
        else:
            return BlogPostCreateSerializer

class BlogCommentListCreate(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'post.pk'
    lookup_url_kwarg = 'post_pk'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCommentCreateSerializer
        else:
            return BlogCommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
