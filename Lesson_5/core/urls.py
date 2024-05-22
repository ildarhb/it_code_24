from django.urls import path
from core import views

urlpatterns = [
    path('', views.ClassBasedIndex.as_view(), name='home'),
    path('category/<int:category_id>', views.ClassBasedCategory.as_view(), name='category'),
    path('posts', views.PostList.as_view(), name='posts'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='posts'),
]