from django.urls import path, include


app_name = 'api'

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('', include('api.auth.urls')),
]
