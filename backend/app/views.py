from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request , "app/home.html")

def jokes(request):
    return render(request , "app/jokes.html")

def articles(request):
    return render(request , "app/articles.html")

def quotes(request):
    return render(request , "app/quotes.html")