from django.urls import path
from django.contrib.auth import views as auth_views
from .views import about, register



urlpatterns = [
    path("register/", register, name="register"),
    path("about/", about, name="about"),
]