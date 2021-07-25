from django.shortcuts import render
from django.utils import timezone
from .models import Blog


def main_page(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/main_page.html', context)


def details(request):
    return render(request, 'blog/details.html')
