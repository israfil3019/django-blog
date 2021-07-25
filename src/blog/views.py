from django.shortcuts import render
from .models import Blog

def main_page(request):
    return render(request, 'blog/main_page.html')

def details(request):
    return render(request, 'blog/details.html')
