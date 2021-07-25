from django.shortcuts import render
from django.utils import timezone
from .models import Blog
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .forms import BlogForm
from django.urls import reverse_lazy
from django.contrib import messages


def main_page(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/main_page.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog": blog
    }
    return render(request, 'blog/blog_detail.html', context)

class BlogDetail(DetailView):
    model = Blog

class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_add.html"  # app/blog_form.html  == suffix  '_form'
    success_url = reverse_lazy('')  # redirect == '//'

class BlogUpdate(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update.html"  # app/blog_form.html  == suffix  '_form'
    # success_url = reverse_lazy('list')
    success_url = '/list/'
    pk_url_kwarg = 'id'

class BlogDelete(DeleteView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_delete.html"  # app/blog_confirm_delete.html 
    success_url = reverse_lazy('list')
    # success_url = '/list/'
    pk_url_kwarg = 'id'
