from django.utils import timezone
from django.db.models import Count

from rest_framework import generics
import datetime

from blog.models import BlogCategory
from blog.serializers.blog_post_serializer import BlogCategorySerializer

class BlogCategoryList(generics.ListAPIView):
	queryset = BlogCategory.objects.all()
	serializer_class = BlogCategorySerializer

class RecentPopularBlogCategoryList(generics.ListAPIView):
	serializer_class = BlogCategorySerializer

	def get_queryset(self):
		one_week_ago = timezone.now() - datetime.timedelta(days=7)
		queryset = BlogCategory.objects.filter(
			posts__pub_date__gte=one_week_ago
		).annotate(
			posts_count=Count('posts')
		).order_by(
			'-posts_count'
		)

		return queryset