from django.contrib.auth import authenticate, login, logout

from rest_framework import response, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from auth.serializers.user_serializer import UserSerializer

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return response.Response({"message": 'Logged out succesfully'}, status=status.HTTP_204_NO_CONTENT)
