from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def register(request):
    form = RegistrationForm(request.POST or None) 
    if request.user.is_authenticated:
        messages.warning(request, "You are already have an account!")
        return redirect("blog:main_page")
    if form.is_valid():
        form.save()
        name = form.cleaned_data["username"]
        messages.success(request, f"Account created for {name}")
        return redirect("login")  
                
    context = {
        "form" : form
    }
    return render(request, "users/register.html", context)

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, instance=request.user.profile, files=request.FILES)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, "Your profile has been updated!")
        return redirect(request.path)
    
    context = {
        "u_form" : u_form,
        "p_form" : p_form    
    }
    return render(request, "users/profile.html", context)


def about(request):
    return render(request, 'users/about.html')