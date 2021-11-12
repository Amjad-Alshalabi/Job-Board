from django.contrib import admin
from .models import blog, Category

# Register your models here.

admin.site.register(blog)
admin.site.register(Category)