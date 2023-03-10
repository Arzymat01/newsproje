from django.shortcuts import render
from .models import News


def index(request):

    search_query = request.GET.get('search', '')

    if search_query:
        news = News.objects.filter(home__contains=search_query)
    else:
        news = News.objects.all().order_by
    news = News.objects.all()
    context = {
        'news': news,

    }

    return render(request, 'website/index.html', context)


def business(request):

    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'website/business.html', context)


def health(request):

    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'website/health.html', context)


def politika(request):

    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'website/politika.html', context)


def sport(request):

    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'website/sport.html', context)


def technology(request):

    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'website/technology.html', context)


def wecome(request):

    return render(request, 'website/wecome.html')
