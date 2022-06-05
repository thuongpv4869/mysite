from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from mysite.api.urls import urlpatterns as api_urlpatterns

app_name = 'mysite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urlpatterns, app_name), namespace='api')),
]

if settings.DEBUG:
    urlpatterns += [

        # open api 3
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/',
             SpectacularSwaggerView.as_view(url_name='schema'),
             name='swagger-ui'),
        path('api/schema/redoc/',
             SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
