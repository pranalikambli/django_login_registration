from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('login', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]