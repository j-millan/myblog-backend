import django_filters
from blog.models import BlogPost

class BlogPostFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    publication_date = django_filters.DateTimeFilter(field_name='pub_date')
    author_id = django_filters.NumberFilter(field_name='author', lookup_expr='pk')
    category_id = django_filters.NumberFilter(field_name='categories', lookup_expr='pk')

    class Meta:
        model = BlogPost
        fields = ['content', 'publication_date', 'author_id', 'category_id']