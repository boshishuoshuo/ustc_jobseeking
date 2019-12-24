from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import JobPosts

@login_required
def home(request):
    context = {
        'posts': JobPosts.objects.all()
    }
    return render(request, 'jobposts/home.html', context)

def about(request):
    return render(request,'jobposts/about.html', {'title': 'About'})