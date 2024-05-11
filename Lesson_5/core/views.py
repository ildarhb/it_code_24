from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context={
        'posts' : posts,
        'categories' : categories,
        'title':'Список статей',
    }

    return render(request, template_name='core/index.html', context=context)

def get_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context={
        'posts' : posts,
        'categories' : categories,
        'category' : category,
    }
    print(context)

    return render(request, template_name='core/category.html', context=context)
