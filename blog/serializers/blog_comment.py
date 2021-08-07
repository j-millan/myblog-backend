from rest_framework import serializers
from blog.models import BlogComment
from blog.serializers.user import UserSerializer

class BlogCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BlogComment
        fields = ['message', 'author', 'post', 'pub_date', 'upd_date']
