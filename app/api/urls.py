from django.urls import path

from .views import PhotoLoader, SecondPhotoLoader


app_name = 'api'


urlpatterns = [
    path('load_photo/', PhotoLoader.as_view(), name='api_photo_loader'),
    path('add_photo/', SecondPhotoLoader.as_view(), name='api_photo_loader'),
]
