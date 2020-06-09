from django.shortcuts import render,get_object_or_404
from newsapi import NewsApiClient
from datetime import datetime
import requests

def Home(request):
    newsapi = NewsApiClient(api_key='81959fd211d94f60bbfd44026bc96104')
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
    'q': 'india economy', # query phrase
    'pageSize': 20,  # maximum is 100
    'apiKey': '81959fd211d94f60bbfd44026bc96104' # your own API key
}
    response = requests.get(url, params=parameters)
    response_json = response.json()
    print(response_json)
    dates = datetime.now().date()

    desc = []
    news = []
    img = []
    url = []

    for i in response_json['articles']:
        news.append(i['title'])
        url.append(i['url'])
        desc.append(i['description'])
        img.append(i['urlToImage'])

    mylist = zip(news, desc, img,url)
    return render(request,"News/news.html",context={"mylist":mylist,'dates':dates})

def News(request):
    url = 'https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey=81959fd211d94f60bbfd44026bc96104'
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    dates = datetime.now().date()

    desc = []
    news = []
    img = []
    url = []

    for i in response_json['articles']:
        news.append(i['title'])
        url.append(i['url'])
        desc.append(i['description'])
        img.append(i['urlToImage'])

    list = zip(news, desc, img,url)
    return render(request,"News/google.html",context={"list":list,'dates':dates})
