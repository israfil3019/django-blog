from django.urls import path
from .views import BlogCreate, BlogDelete, BlogDetail, BlogUpdate, main_page

app_name = 'blog'

urlpatterns = [
    path('', main_page, name='main_page'),
    # path("<int:id>/", details, name="details"),
    path("add/", BlogCreate.as_view(), name="add"),
    path("<int:id>/detail", BlogDetail.as_view(), name="detail"),
    path("<int:id>/update/", BlogUpdate.as_view(), name="update"),
    path("<int:id>/delete/", BlogDelete.as_view(), name="delete"),
]
