from rest_framework import generics 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from blog.models import UserFollowing
from blog.serializers.user_following_serializer import UserFollowingSerializer, UserFollowingCreateSerializer
from blog.filters import UserFollowingFilter
from blog.permissions import IsUserFollowing

class UserFollowingListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return UserFollowingFilter(
            self.request.GET, UserFollowing.objects.all()).qs
    
    def get_serializer_class(self):
        if self.request.method  == 'POST':
            return UserFollowingCreateSerializer
        else:
            return UserFollowingSerializer
    
    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class UserFollowingDelete(generics.DestroyAPIView):
    queryset = UserFollowing.objects.all()
    permission_classes = [IsAuthenticated, IsUserFollowing]