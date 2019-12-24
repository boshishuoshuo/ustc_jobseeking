from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jobposts-home'),
    path('about', views.about, name='jobposts-about')
]