from datetime import datetime
from django.test import Client, TestCase
from django.urls import reverse
from api.common import ApiResponseBody

from core.models.user import UserFullInfo


class TestGetUserProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = self.create_user()

    @staticmethod
    def create_user():
        user = UserFullInfo(
            email="test@user.com",
            first_name='elon',
            last_name='musk',
            date_of_birth=datetime.now(),
            is_active=True,
            is_superuser=False,
            is_admin=False
        )
        user.set_password('test')
        user.full_clean()
        user.save()
        return user

    def test_get_user_info(self):
        response = self.client.get(
            reverse('api:user:user_profile',
                    kwargs={
                        "user_id": self.user.id
                    })
        )

        self.assertEqual(response.status_code, 200)

        expected_body = ApiResponseBody(
            data={
                "id": self.user.id,
                "email": self.user.email,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
            }).json()

        self.assertEqual(response.json(), expected_body)
