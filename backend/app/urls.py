from django.urls import path

from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("jokes" , views.jokes , name="jokes"),
    path("articles" , views.articles,name="articles"),
    path("quotes" , views.quotes,name="quotes")
]