from django.contrib import admin
from core import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Category)