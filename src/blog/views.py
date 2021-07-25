from django.shortcuts import render

def details(request):
    return render(request, 'blog/details.html')
