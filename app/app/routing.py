from django.urls import re_path

from photos.consumers import PhotoConsumer

websocket_urlpatterns = [
    re_path(r"ws/photos/$", PhotoConsumer.as_asgi()),
]
