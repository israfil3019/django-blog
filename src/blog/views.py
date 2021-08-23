from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Blog, Like, BlogView, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView

class BlogList(ListView):
    model = Blog
    template_name = "blog/main_page.html"
    context_object_name = 'blogs'

@login_required()
def blog_add(request):
    # form = BlogForm(request.POST or None, request.FILES or None)
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        # print(request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "Blog created successfully!")
            return redirect("blog:main_page")
    context = {
        'form' : form
    }
    return render (request, "blog/blog_add.html", context)

def blog_detail(request, slug):
    form = CommentForm()
    obj = get_object_or_404(Blog, slug=slug)
    if request.user.is_authenticated:
        BlogView.objects.get_or_create(user=request.user, blog=obj)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = obj
            comment.save()
            return redirect("blog:detail", slug=slug)
    context = {
        'object' : obj,
        "form" : form,
    }
    return render(request, "blog/blog_detail.html", context)

@login_required()
def blog_update(request, slug):
    obj = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None, request.FILES or None, instance=obj)
    if request.user.id != obj.author.id:
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not an author of this blog!")
        return redirect("blog:main_page")
    if form.is_valid():
        form.save()
        messages.success(request, "Blog updated !!")
        return redirect("blog:main_page")
    context = {
        "object" : obj,
        "form" : form
    }
    return render(request, "blog/blog_update.html", context)

@login_required()
def blog_delete(request, slug):
    obj = get_object_or_404(Blog, slug=slug)
    if request.user.id != obj.author.id:
        # return HttpResponse("You are not authorized!")
        messages.warning(request, "You are not an author of this blog!")
        return redirect("blog:main_page")
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Blog deleted !!")
        return redirect("blog:main_page")
    
    context = {
        "object" : obj
    }
    return render(request, "blog/blog_delete.html", context)

@login_required()
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Blog, slug=slug)
        like_qs = Like.objects.filter(user=request.user, blog=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, blog=obj)
        return redirect("blog:detail", slug=slug)
    return redirect("blog:detail", slug=slug)


