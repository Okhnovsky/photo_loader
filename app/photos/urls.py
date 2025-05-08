from django.urls import path

from .views import index


app_name = 'photos'


urlpatterns = [
    path('', index, name='index')
]
