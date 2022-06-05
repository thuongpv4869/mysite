from django.urls import path

from mysite.api.user import views


urlpatterns = [
    path('<int:user_id>/profile',
         views.UserProfileView.as_view(), name='user_profile'),
    path('profile',
         views.CurrentUserProfileView.as_view(), name='current_user_profile'),
]
