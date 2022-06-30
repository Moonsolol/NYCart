from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register_new_user/', views.register_new_user, name='useradmin_register'),
    path('login/', auth_views.LoginView.as_view(template_name='useradmin\login.html'),name='useradmin_login'),
    path('logout/', auth_views.LogoutView.as_view(),name='useradmin_logout'),
]