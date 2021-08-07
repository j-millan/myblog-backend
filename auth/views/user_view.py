from django.contrib.auth.models import User

from rest_framework import generics

from auth.serializers.user_serializer import UserSerializer, UserCreateSerializer, UserUpdateSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        else:
            return UserSerializer