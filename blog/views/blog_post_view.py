from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogPost
from blog.serializers.blog_post_serializer import BlogPostSerializer, BlogPostCreateSerializer
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

class UserBlogPostList(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    
    def get_queryset(self):
        return BlogPost.objects.filter(author__pk=self.kwargs['user_pk'])

class BlogPostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogPostSerializer
        else:
            return BlogPostCreateSerializer
