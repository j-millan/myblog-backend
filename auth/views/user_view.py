from django.contrib.auth.models import User

from rest_framework import generics

from auth.serializers.user_serializer import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from auth.permissions import IsUserAuthenticatedOrReadOnly
from auth.models import UserProfile

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        else:
            return UserSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        UserProfile.objects.create(user=serializer.instance)

class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsUserAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UserUpdateSerializer
        else:
            return UserSerializer