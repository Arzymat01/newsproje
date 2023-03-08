from django.contrib import admin
from django.urls import path, re_path
from .views import updates, add, update, delete, load_more
urlpatterns = [
    path('updates/', updates, name='updates'),
    path('add', add, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('load-more', load_more, name='load-more'),


]
