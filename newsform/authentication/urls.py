from django.contrib import admin
from django.urls import path, re_path
from .views import login_request, register_request, dashboard
urlpatterns = [
    path('',  login_request, name='login'),
    path('register/', register_request, name='register'),
    path('dashboard', dashboard, name='dashboard'),

]
