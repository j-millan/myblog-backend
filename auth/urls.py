from django.urls import path

from auth.views import user_view

app_name = 'auth'

urlpatterns = [
    path('login', user_view.user_login, name='login'),
    path('logout', user_view.user_logout, name='logout'),
    path('users', user_view.UserListCreate.as_view(), name='user_list_create'),
    path('users/<int:pk>', user_view.UserDetailUpdateDelete.as_view(), name='user_detail_update_delete'),
    path('users/update-profile', user_view.UserProfileInformationUpdate.as_view(), name='user_profile_update'),  
]