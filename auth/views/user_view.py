from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import response, status

from auth.serializers.user_serializer import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from auth.serializers.user_profile_serializer import UserProfileSerializer
from auth.permissions import IsUserAuthenticatedOrReadOnly
from auth.models import UserProfile

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        raise AuthenticationFailed

    return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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

class UserProfileInformationUpdate(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)
