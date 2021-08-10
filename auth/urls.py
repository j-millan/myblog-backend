from django.urls import path

from auth.views import user_view
from auth.views import authentication_view

app_name = 'auth'

urlpatterns = [
    path('register', authentication_view.UserRegister.as_view(), name='register'),
    path('login', authentication_view.user_login, name='login'),
    path('logout', authentication_view.user_logout, name='logout'),
    path('users', user_view.UserList.as_view(), name='user_list_create'),
    path('users/<int:pk>', user_view.UserDetailUpdateDelete.as_view(), name='user_detail_update_delete'),
    path('users/update-profile', user_view.UserProfileInformationUpdate.as_view(), name='user_profile_update'),  
]