from django.urls import path

from auth.views import user_view

app_name = 'auth'

urlpatterns = [
  path('users/', user_view.UserListCreate.as_view(), name='user_list_create'),
  path('users/<int:pk>/', user_view.UserDetailUpdateDelete.as_view(), name='user_detail_update_delete'),
]