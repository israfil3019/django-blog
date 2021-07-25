from django.urls import path
from .views import details, main_page

app_name = 'blog'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('details/', details, name='details'),
]
