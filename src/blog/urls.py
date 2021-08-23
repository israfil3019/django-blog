from django.urls import path
from .views import BlogList, blog_add, blog_detail, blog_update, blog_delete, like
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"
urlpatterns = [
    path('', BlogList.as_view(), name='main_page'),
    path("create/",blog_add, name="add"),
    path("<str:slug>/",blog_detail, name="detail"),
    path("<str:slug>/update/",blog_update, name="update"),
    path("<str:slug>/delete/",blog_delete, name="delete"),
    path("<str:slug>/like/",like, name="like"),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
