from datetime import datetime
from django.test import Client, TestCase
from django.urls import reverse
from api.common import ApiResponseBody

from core.models.user import UserFullInfo


class TestLogin(TestCase):
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

    def test_login(self):
        response = self.client.post(
            reverse('api:auth:login'),
            data={
                "email": self.user.email,
                "password": "test"
            }
        )

        self.assertEqual(response.status_code, 200)

        response_body = ApiResponseBody.from_json(response.json())

        expected_body = ApiResponseBody(
            data={
                "id": self.user.id,
                "email": self.user.email,
                "access_token": "",
                "refresh_token": "",
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
            })

        self.assertEqual(response_body.data.keys(), expected_body.data.keys())
