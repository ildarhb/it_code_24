from django.urls import path
from rest_framework.routers import DefaultRouter
from core import views

urlpatterns = [
    path('', views.ClassBasedIndex.as_view(), name='home'),
    path('category/<int:category_id>', views.ClassBasedCategory.as_view(), name='category'),
    path('posts', views.PostList.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='posts'),

    path('posts_api', views.PostAPIView.as_view(), name='posts_api'),
]

app_name = 'core'

router = DefaultRouter()
router.register('posts_set', views.PostModelViewSet, basename='posts_set')

urlpatterns += router.urls