from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogComment
from blog.serializers.blog_comment_serializer import BlogCommentSerializer, BlogCommentCreateSerializer, BlogCommentUpdateSerializer
from blog.permissions import IsOwnerOrReadOnly
from blog.filters import BlogCommentFilter

class BlogCommentListCreate(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        comments = BlogCommentFilter(self.request.GET, BlogComment.objects.all())
        return comments.qs

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogCommentCreateSerializer
        else:
            return BlogCommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
