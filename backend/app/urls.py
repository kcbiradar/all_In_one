from django.urls import path

from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("addJoke" , views.addJoke , name="addJoke"),
    path("addArticle" , views.addArticle , name="addArticle"),
    path("addQuote" , views.addQuote , name= "addQuote"),
    path("jokes" , views.jokes , name="jokes"),
    path("articles" , views.articles,name="articles"),
    path("quotes" , views.quotes,name="quotes")
]