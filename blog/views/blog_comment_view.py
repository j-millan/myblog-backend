from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogComment
from blog.serializers.blog_comment_serializer import BlogCommentSerializer, BlogCommentCreateSerializer, BlogCommentUpdateSerializer

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
