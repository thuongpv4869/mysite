from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', include('mysite.urls', namespace='mysite'))
]

if settings.DEBUG:
    urlpatterns += [
        path('debug/', include('debug_toolbar.urls'))
    ]
