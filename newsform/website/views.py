from django.shortcuts import render
from .models import News
import requests
from newsapi import NewsApiClient


def index(request):

    newsapi_key = "10295f4657ce4101b8697efa2fec8d97"

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)

    search_query = request.GET.get('search', '')

    if search_query:
        news = News.objects.filter(home__contains=search_query)
    else:
        news = News.objects.all().order_by
    news = News.objects.all()
    context = {
        'mylist': mylist,
        'news': news,

    }

    return render(request, 'website/index.html', context)


def business(request):
    newsapi_key = "10295f4657ce4101b8697efa2fec8d97"

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi_key}"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)

    news = News.objects.all()
    context = {
        'mylist': mylist,
        'news': news
    }
    return render(request, 'website/business.html', context)


def health(request):
    newsapi_key = "10295f4657ce4101b8697efa2fec8d97"
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={newsapi_key}"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)

    news = News.objects.all()
    context = {
        'mylist': mylist,
        'news': news
    }
    return render(request, 'website/health.html', context)


def politika(request):
    newsapi_key = "10295f4657ce4101b8697efa2fec8d97"

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={newsapi_key}"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)

    news = News.objects.all()
    context = {
        'news': news,
        'mylist': mylist,
    }
    return render(request, 'website/politika.html', context)


def sport(request):
    newsapi_key = "10295f4657ce4101b8697efa2fec8d97"

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=sport&apiKey={newsapi_key}"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)

    news = News.objects.all()

    context = {
        'news': news,
        'mylist': mylist,


    }
    return render(request, 'website/sport.html', context)


def technology(request):

    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=10295f4657ce4101b8697efa2fec8d97"

    c_news = requests.get(url).json()
    a = c_news['articles']
    desc = []
    title = []
    img = []
    pbl = []
    ctn = []
    ur = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pbl.append(f['publishedAt'])
        ctn.append(f['content'])
        ur.append(f['url'])

    mylist = zip(title, desc, img, pbl, ctn, ur)
    news = News.objects.all()
    context = {
        'news': news,
        'mylist': mylist,
    }
    return render(request, 'website/technology.html', context)


def wecome(request):

    return render(request, 'website/wecome.html')

# def newsapi(request):
#     newsapi_key = "10295f4657ce4101b8697efa2fec8d97"
#     url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
#     main_page=request.get(url)=json()


# newsapi_key = "10295f4657ce4101b8697efa2fec8d97"
# url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"

# url = "https://newsapi.org/v2/top-headlines"
# params = {
#     "country": "ru",
#     "apiKey": "10295f4657ce4101b8697efa2fec8d97"
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     articles = data["articles"]
#     for article in articles:
#         print(article["title"])
# else:
#     print("Failed to fetch news")
