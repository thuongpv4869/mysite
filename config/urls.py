from django.conf import settings
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('mysite.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('debug/', include('debug_toolbar.urls')),
        path('admin/', admin.site.urls),
    ]
