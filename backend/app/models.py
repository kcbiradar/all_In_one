from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

ARTICLE_TYPE = (
    ('SCIENCE' , 'SCIENCE'),
    ('MATH' , 'MATHESMATICS'),
    ('TECH' , 'TECHNOLOGY'),
    ('STORY' , 'STORY'),
    ('ART' , 'ART'),
)

class Jokes(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False,blank=False)
    joke = models.CharField(max_length=200,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Articles(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False,blank=False)
    article = models.CharField(max_length=2000,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    article_type = models.CharField(max_length=20,choices=ARTICLE_TYPE,null=False,blank=False)

    def __str__(self):
        return self.title + " " + self.article_type

class Quote(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False,blank=False)
    quote = models.CharField(max_length=2000,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)


