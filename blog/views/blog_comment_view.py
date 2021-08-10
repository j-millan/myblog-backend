from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogComment
from blog.serializers.blog_comment_serializer import BlogCommentSerializer, BlogCommentCreateSerializer, BlogCommentUpdateSerializer
from blog.permissions import IsOwnerOrReadOnly
from blog.filters import BlogCommentFilter

class BlogCommentListCreate(generics.ListCreateAPIView):
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

class BlogCommentUpdateDelete(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
