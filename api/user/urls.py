from django.urls import path

from api.user import views

app_name = 'user'

urlpatterns = [
    path('<int:user_id>/profile',
         views.UserProfileView.as_view(), name='user_profile'),
]
