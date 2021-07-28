from django.urls import path
from .views import about, register, user_login, user_logout, profile

app_name = 'users'

urlpatterns = [

    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('user_login/', user_login, name='user_login'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
]
