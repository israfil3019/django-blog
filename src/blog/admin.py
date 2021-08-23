from django.contrib import admin
from .models import  Blog, Comment, Like, BlogView, Category

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogView)
admin.site.register(Like)

