from django.contrib.auth import authenticate, login, logout

from rest_framework import response, status, generics, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

from auth.serializers.user_serializer import UserSerializer, UserCreateSerializer
from auth.models import UserProfile

def get_response_with_token(serializer):
    data = serializer.data
    token = Token.objects.get_or_create(user=serializer.instance)[0]
    user_data = {
        'token': token.key,
        'user': {
            'id': data['id'],
            'username': data['username'],
            'email': data['email'],
        }
    }

    return user_data

class UserRegister(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            login(request, serializer.instance)
            user_data = get_response_with_token(serializer)
            UserProfile.objects.create(user=serializer.instance)

            return response.Response(user_data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            user_data = get_response_with_token(
                UserSerializer(user))
            return response.Response(user_data, status=status.HTTP_200_OK)

        raise AuthenticationFailed

    return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return response.Response({"message": 'Logged out successfully'}, status=status.HTTP_204_NO_CONTENT)
