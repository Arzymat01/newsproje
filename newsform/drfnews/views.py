from django.shortcuts import render
from rest_framework import generics
from website.models import News
from .serializer import NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class NewsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        lst = News.objects.all().values()
        return Response({'website': list(lst)})

    def post(self, request, format=None):
        return Response({'city': 'Bishkek'})


# class NewsApiView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
