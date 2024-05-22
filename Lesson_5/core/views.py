from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post, Category


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
