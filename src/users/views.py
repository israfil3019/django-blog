from django.shortcuts import render, redirect, HttpResponse
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User

# login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages




def register(request):
    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)

    
    if form_user.is_valid():
        user = form_user.save()
        profile = form_profile.save(commit=False)
        profile.user = user

        if 'profile_pics' in request.FILES:
            profile.profile_pics = request.FILES['profile_pics']

        profile.save()

        messages.success(request, "Register successful")
        return redirect('blog:main_page')

    context = {
        'form_user': form_user,
        'form_profile': form_profile,
    }

    return render(request, 'users/register.html', context)


@login_required
def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('blog:main_page')


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                messages.success(request, "Login successful")
                login(request, user)
                return redirect('blog:main_page')
            else:
                messages.error(request, "Account is not active")
                return render(request, 'users/user_login.html', {"form": form})
        else:
            messages.error(request, "Password or Username is wrong!")
            return render(request, 'users/user_login.html', {"form": form})
    return render(request, 'users/user_login.html', {"form": form})


def profile(request):
    return render(request, 'users/profile.html')

