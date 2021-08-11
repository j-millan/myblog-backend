from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import UserFollowing
from auth.serializers.user_serializer import UserSerializer

class UserFollowingSerializer(serializers.ModelSerializer):
    follower = UserSerializer()
    followed = UserSerializer()
    
    class Meta:
        model = UserFollowing
        fields = ['follower', 'followed', 'date_followed']
        read_only_fields = ['__all__']

class UserFollowingCreateSerializer(serializers.ModelSerializer):
    follower_id = serializers.ReadOnlyField(source='follower.id')
    followed_user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='followed'
    )

    class Meta:
        model = UserFollowing
        fields = ['id', 'follower_id', 'followed_user_id', 'date_followed']
        read_only_fields = ['id', 'date_followed', 'follower_id']
