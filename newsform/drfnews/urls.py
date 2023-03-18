from django.urls import path, include, re_path
from .views import NewsApiView, ContactAPIView

urlpatterns = [
    path('websitelist/', NewsApiView.as_view()),
    path("contactslist/", ContactAPIView.as_view()),
    path("new/<str:pk>", NewsApiView.as_view()),

]
