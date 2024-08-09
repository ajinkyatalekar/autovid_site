from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('register_user/', views.register_user, name="register_user"),
    path('user_home/', views.user_home, name="user_home"),
    path('logout_user/', views.logout_user, name="logout_user"),
]