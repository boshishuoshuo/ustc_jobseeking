from django.shortcuts import render
from .models import JobPosts

def home(request):
    context = {
        'posts': JobPosts.objects.all()
    }
    return render(request, 'jobposts/home.html', context)

def about(request):
    return render(request,'jobposts/about.html', {'title': 'About'})