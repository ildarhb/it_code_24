from django.urls import path
from core import views

urlpatterns = [
    path('', views.ClassBasedIndex.as_view(), name='home'),
    path('category/<int:category_id>', views.get_category, name='category'),
]