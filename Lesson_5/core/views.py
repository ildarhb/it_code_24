from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Category
from .serilizers import PostSerializer
from .filters import PostFilter

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class ClassBasedIndex(TemplateView):
    template_name='core/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        posts = Post.objects.all()
        categories = Category.objects.all()
        
        context['posts'] = posts
        context['categories'] = categories
        context['title'] = 'Список статей'

        return context


class ClassBasedCategory(TemplateView):
    template_name='core/category.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        category_id = self.kwargs.get('category_id', None)
        posts = Post.objects.filter(category=category_id)
        categories = Category.objects.all()
        category = Category.objects.get(pk=category_id)
        
        context['posts'] = posts
        context['categories'] = categories
        context['category'] = category

        return context


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'core/post_list.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'core/post_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context['info'] = 'Автор стати - Иванов'
        return context
    

class PostAPIView(APIView):
    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})


class PostModelViewSet(ModelViewSet):
    qs = Post.objects.all()
    filterset_class = PostFilter
    serializer_class = PostSerializer
