from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('select_posts', views.home, name="select_posts"),
    path('about', views.home, name="about"),
]