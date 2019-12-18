from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='job-posts'),
    path('about', views.about, name='about-ustc-jobseeking')
]