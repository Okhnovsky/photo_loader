from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photos.urls', namespace='photos')),
    path('api/', include('api.urls', namespace='api')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
