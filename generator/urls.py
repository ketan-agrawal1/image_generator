from django.urls import path
from .views import generate_images

urlpatterns = [
    path('', generate_images, name='generate_images'),
]
