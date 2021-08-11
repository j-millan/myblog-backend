import django_filters
from blog.models import BlogPost, BlogComment, UserFollowing

class BlogPostFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    publication_date = django_filters.DateTimeFilter(field_name='pub_date')
    author_id = django_filters.NumberFilter(field_name='author', lookup_expr='pk')
    category_id = django_filters.NumberFilter(field_name='categories', lookup_expr='pk')

    class Meta:
        model = BlogPost
        fields = ['content', 'publication_date', 'author_id', 'category_id']

class BlogCommentFilter(django_filters.FilterSet):
    author_id = django_filters.NumberFilter(field_name='author', lookup_expr='pk')
    post_id = django_filters.NumberFilter(field_name='post', lookup_expr='pk')

    class Meta:
        model = BlogComment
        fields = ['author_id', 'post_id']

class UserFollowingFilter(django_filters.FilterSet):
    follower_id = django_filters.NumberFilter(field_name='follower', lookup_expr='pk')
    followed_id = django_filters.NumberFilter(field_name='followed', lookup_expr='pk')

    class Meta:
        model = UserFollowing
        fields = ['follower_id', 'followed_id']