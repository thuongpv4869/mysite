from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone

from mysite.models import UserFullInfo


class TestGetCurrentProfileApi(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = self.create_user()
        self.client.force_authenticate(user=self.user)

    def test_get_current_profile(self):
        url = reverse('mysite:api:v1:user:current_user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @staticmethod
    def create_user():
        user = UserFullInfo(
            email="test@user.com",
            first_name='elon',
            last_name='musk',
            date_of_birth=timezone.now(),
            is_active=True,
            is_superuser=False,
            is_admin=False
        )
        user.set_password('test')
        user.full_clean()
        user.save()
        return user
