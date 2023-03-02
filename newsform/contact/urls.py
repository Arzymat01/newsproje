from django.contrib import admin
from django.urls import path, re_path
from .views import contact
urlpatterns = [
    path('contact/',  contact, name='contact'),


]
