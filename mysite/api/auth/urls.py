from django.urls import path

from mysite.api.auth import views


urlpatterns = [
    path('login',
         views.LoginView.as_view(), name='login'),
]
