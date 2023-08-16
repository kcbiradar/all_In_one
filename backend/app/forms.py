from django import forms
from django.forms import ModelForm

from . import models

class AddJokeForm(ModelForm):
    class Meta:
        model = models.Jokes
        fields = ["title" , "joke"]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'joke' : forms.Textarea(attrs={'class' : 'form-control'})
        }

class AddArticleForm(ModelForm):
    class Meta:
        model = models.Articles
        fields = ["title" , "article" , "article_type"]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'article' : forms.Textarea(attrs={'class' : 'form-control'}),
            'article_type' : forms.Select(attrs={'class' : 'form-control'})
        }

class AddQuoteForm(ModelForm):
    class Meta:
        model = models.Quote
        fields = ["title" , "quote"]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'quote':forms.Textarea(attrs={'class' : 'form-control'})
        }

