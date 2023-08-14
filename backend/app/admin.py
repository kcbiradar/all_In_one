from django.contrib import admin

from . import models

admin.site.register(models.User)

admin.site.register(models.Jokes)

admin.site.register(models.Articles)

admin.site.register(models.Quote)
