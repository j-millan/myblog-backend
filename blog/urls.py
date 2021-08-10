from django.urls import path

from blog.views import blog_post_view, blog_comment_view

app_name = 'blog'

urlpatterns = [
    path('blog-posts', blog_post_view.BlogPostListCreate.as_view(), name='blog_post_list'),
    path('blog-posts/<int:pk>/', blog_post_view.BlogPostDetailUpdateDelete.as_view(), name='blog_post_detail'),
    path('blog-comments', blog_comment_view.BlogCommentListCreate.as_view(), name='blog_comment_list'),
]