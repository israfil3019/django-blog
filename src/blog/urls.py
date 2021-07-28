from django.urls import path
from .views import BlogCreate, BlogDelete, BlogDetail, BlogList, BlogUpdate
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view(), name='main_page'),
    path("add/", BlogCreate.as_view(), name="add"),
    path("<int:pk>/detail", BlogDetail.as_view(), name="detail"),
    path("<int:id>/update/", BlogUpdate.as_view(), name="update"),
    path("<int:id>/delete/", BlogDelete.as_view(), name="delete"),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
