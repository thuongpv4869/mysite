from rest_framework.views import APIView, status
# from rest_framework import serializers as drf_serializers
from api.auth import serializers
from api.common import get_api_response
from drf_spectacular.utils import (
    extend_schema,
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):

    @extend_schema(
        request=serializers.LoginSerializer,
        responses={200: serializers.LoginResponseDataSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = authenticate(**serializer.validated_data)
            if not user:
                # TODO: raise exception
                pass

            refresh = RefreshToken.for_user(user)

            data = serializers.LoginResponseDataSerializer(user, refresh)\
                              .to_json()

        return get_api_response(data, status=status.HTTP_200_OK)
