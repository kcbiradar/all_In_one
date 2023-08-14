from django.urls import path

from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("jokes" , views.jokes , name="joke"),
    path("articles" , views.articles,name="article"),
    path("quotes" , views.quotes,name="quotes")
]