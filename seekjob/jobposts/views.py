from django.shortcuts import render

posts = [
    {
        'author': 'Yan Feng',
        'title': 'Job post 1',
        'content': 'First job post',
        'date_posted': 'Dec 17, 20190'
    },
{
        'author': 'Ru Yan',
        'title': 'Job post 2',
        'content': 'Second job post',
        'date_posted': 'Dec 16, 20190'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'jobposts/home.html', context)

def about(request):
    return render(request,'jobposts/about.html', {'title': 'About'})