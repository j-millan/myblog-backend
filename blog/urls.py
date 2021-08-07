from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
  path('blog-posts/', views.BlogPostListCreate.as_view(), name='blog_post_list'),
  path('blog-posts/<int:pk>/', views.BlogPostDetailUpdateDelete.as_view(), name='blog_post_detail'),
  path('blog-comments/<int:post_pk>/', views.BlogCommentListCreate.as_view(), name='blog_comment_list'),
]