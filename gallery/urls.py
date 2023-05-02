from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import *
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', display_images, name = 'display_images'),
    path('image_upload', image_upload, name = 'image_upload'),
    path('success', success, name = 'success'),
]
