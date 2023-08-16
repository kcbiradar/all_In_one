from django.shortcuts import render

from django.http import HttpResponse

from . import forms

from . import models

def home(request):
    return render(request , "app/home.html")


def addJoke(request):
    return render(request , "app/addJoke.html" , {
        "form" : forms.AddJokeForm()
    })

def addArticle(request):
    return render(request , "app/addArticle.html" , {
        "form" : forms.AddArticleForm()
    })

def addQuote(request):
    return render(request , "app/addQuote.html" , {
        "form" : forms.AddQuoteForm()
    })

def jokes(request):
    return render(request , "app/jokes.html" , {
        "jokes" : models.Jokes.objects.all()
    })

def articles(request):
    return render(request , "app/articles.html")

def quotes(request):
    return render(request , "app/quotes.html")