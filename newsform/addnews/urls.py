from django.contrib import admin
from django.urls import path, re_path
from .views import addnews
urlpatterns = [
    path('addnews/', addnews, name='addnews'),

]
