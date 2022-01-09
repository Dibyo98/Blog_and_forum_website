from django.shortcuts import render
from .models import Post

def home(request):
    contents = {
        'posts': Post.objects.all(),
        'title': 'Forum Home'
    }
    return render(request, 'forum/home.html', contents)

def about(request):
    return render(request, 'forum/about.html', {'title': 'Forum About'})
