import django_filters

from core.models import Post

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        exclude = ('photo',)