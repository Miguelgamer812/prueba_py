from django.urls import path
from .views import segundo_item, create_blog, delete_data
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', segundo_item, name='segundo_item'),
    path('create',create_blog, name='create_blog'),
    path('image_upload', segundo_item, name='image_upload'),
    path('delete/<int:pk>', delete_data, name='delete_data'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)