from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
  path('blog-posts/', views.BlogPostListCreate.as_view(), name='blog_post_list'),
  path('blog-posts/<slug:post_slug>/', views.BlogPostDetailUpdateDelete.as_view(), name='blog_post_detail'),
]