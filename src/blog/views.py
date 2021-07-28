from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Blog
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from .forms import BlogForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

    def form_valid(self, form):
        messages.success(self.request, 'Blog updated successfully')
        return super().form_valid(form)

class BlogDelete(DeleteView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_delete.html"  # app/blog_confirm_delete.html 
    success_url = '/blog/'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Blog deleted successfully')
        return super().form_valid(form)

class BlogList(ListView):
    model = Blog
    template_name = "blog/main_page.html"
    context_object_name = 'blogs'

class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = 'blog'
