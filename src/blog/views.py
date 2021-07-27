from django.shortcuts import render
from django.utils import timezone
from .models import Blog
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .forms import BlogForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def main_page(request):
    blogs = Blog.objects.filter().order_by('created_date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/main_page.html', context)



class BlogDetail(DetailView):
    model = Blog


class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_add.html"  # app/blog_form.html  == suffix  '_form'
    success_url = '/blog/'

class BlogUpdate(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update.html"  # app/blog_form.html  == suffix  '_form'
    success_url = '/blog/'
    pk_url_kwarg = 'id'

class BlogDelete(DeleteView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_delete.html"  # app/blog_confirm_delete.html 
    success_url = '/blog/'
    pk_url_kwarg = 'id'

