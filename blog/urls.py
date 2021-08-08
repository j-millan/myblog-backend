from django.urls import path

from blog.views import blog_post_view, blog_comment_view

app_name = 'blog'

urlpatterns = [
    path('blog-posts/', blog_post_view.BlogPostListCreate.as_view(), name='blog_post_list'),
    path('blog-posts/<int:pk>/', blog_post_view.BlogPostDetailUpdateDelete.as_view(), name='blog_post_detail'),
    path('blog-posts/get-by-user-id/<int:user_pk>/', blog_post_view.UserBlogPostList.as_view(), name='user_blog_post_list'),
    path('blog-comments/<int:post_pk>/', blog_comment_view.BlogCommentListCreate.as_view(), name='blog_comment_list'),
]