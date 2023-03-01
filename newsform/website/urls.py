from django.contrib import admin
from django.urls import path, re_path
from .views import index, business, health, politika, technology, sport, contact

urlpatterns = [

    path('home/', index, name='home'),
    path('health/', health, name='health'),
    path('business/', business, name='business'),
    path('politika/', politika, name='politika'),
    path('technology/', technology, name='technology'),
    path('sport/', sport, name='sport'),
    path('contact/', contact, name='contact'),


]
