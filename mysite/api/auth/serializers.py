# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
# from django.contrib.auth import authenticate, get_user_model
from drf_spectacular.utils import (
    extend_schema_serializer,
)
# from django.utils.translation import gettext as _

# from mysite.models import User


@extend_schema_serializer(
    component_name="LoginRequest",
)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    # def validate_email(self, attr):
    #     raise exceptions.ValidationError(detail=_('email already exists'), code="duplicate")

    def validate(self, attrs):
        # TODO: check valid before check auth
        return attrs


@extend_schema_serializer(
    component_name="LoginResponse",
)
class LoginResponseDataSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    first_name = serializers.CharField()
    refresh_token = serializers.CharField()
    access_token = serializers.CharField()

    def __init__(self, user=None, refresh=None, data=..., **kwargs):
        super().__init__(None, data, **kwargs)
        self.user = user
        self.refresh = refresh

    def to_json(self):
        user = self.user
        profile = self.user.userprofile
        refresh = self.refresh
        data = {
            "id": user.id,
            "email": user.email,
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token)
        }
        return data
