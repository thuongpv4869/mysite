from django.urls import path

from api.user import views

app_name = 'user'

urlpatterns = [
    path('profile', views.UserProfile.as_view(), name='profile'),
]
