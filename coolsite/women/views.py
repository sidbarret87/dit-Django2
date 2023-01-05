from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, catid):
    print("Test 2")
    return HttpResponse(f"<h1>Статьи  по категориям<br>{catid}.</h1>")