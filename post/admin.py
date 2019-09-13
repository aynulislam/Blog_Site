

# Register your models here.

from django.contrib import admin
from . models import Article

# To register this Article Model in our Admin interface
admin.site.register(Article)