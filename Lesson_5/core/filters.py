import django_filters

from core.models import Post, Category

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter("Заголовок", lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date', label="Дата", lookup_expr='lt')
    like_from = django_filters.NumberFilter(field_name='like', label="Лайки", lookup_expr='gt')
    class Meta:
        model = Post
        exclude = ('photo',)

class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter("Заголовок", lookup_expr='icontains')
    class Meta:
        model = Post
        exclude = ('photo',)