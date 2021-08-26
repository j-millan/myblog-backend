from rest_framework import generics

from blog.models import BlogCategory
from blog.serializers.blog_post_serializer import BlogCategorySerializer

class BlogCategoryList(generics.ListAPIView):
	queryset = BlogCategory.objects.all()
	serializer_class = BlogCategorySerializer
