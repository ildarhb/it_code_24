from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, template_name='core/index.html', context={'posts' : posts, 'title':'Список статей'})