from django.urls import path
from .views import segundo_item, create_blog

urlpatterns = [
    path('', segundo_item, name='segundo_item'),
    path('create',create_blog, name='create_blog'),]