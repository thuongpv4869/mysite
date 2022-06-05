from django.urls import path, include
from mysite.api.user.urls import urlpatterns as user_urls
from mysite.api.auth.urls import urlpatterns as auth_urls

app_namespace = 'mysite'

urlpatterns_v1 = [
    path('user/', include((user_urls, app_namespace), namespace='user')),
    path('', include((auth_urls, app_namespace), namespace='auth')),
]

urlpatterns = [
    path('v1/', include((urlpatterns_v1, app_namespace), namespace='v1')),
]
