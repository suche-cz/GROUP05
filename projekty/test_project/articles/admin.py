from django.contrib import admin
from articles import models

admin.site.register(models.Article)
admin.site.register(models.Comment)
