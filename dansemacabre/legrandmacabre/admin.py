from django.contrib import admin
from .models import Artist, Category, Image


# Register your models here.
admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Image)
