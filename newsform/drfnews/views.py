from django.shortcuts import render
from rest_framework import generics
from website.models import News
from .serializer import NewsSerializer, NewsViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from contact.models import Contact_us
from django.forms import model_to_dict



class NewsApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

        # lst = News.objects.all().values()
        # return Response({'website': list(lst)})

        # def post(self, request, format=None):
        #     return Response({'city': 'Bishkek'})


class NewsView(APIView):
    permission_classes=[IsAuthenticated]
    def ger(self,request,pk):
        new=News.objects.get(id=pk)
        serializer = NewsViewSerializer(new)

        return(serializer.data)


class ContactAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        lst = Contact_us.objects.all().values()
        return Response({'contacts': list(lst)})

    def post(self, request, format=None):
        contact_create = Contact_us.objects.create(
            full_name=request.data['full_name'],
            email=request.data['email'],
            message=request.data['message'],
        )
        return Response({'contacts': model_to_dict(contact_create)})


# class NewsApiView(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
