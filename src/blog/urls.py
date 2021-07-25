from django.urls import path
from .views import details

app_name = 'blog'

urlpatterns = [
    path('details/', details, name='details')
]
