from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import (
    extend_schema
)
from mysite.api.common import get_api_response, get_model_serializer

from mysite.models import UserFullInfo


class UserProfileView(APIView):

    serializer_cls = get_model_serializer(
        UserFullInfo,
        list_field=['id', 'email', 'first_name', 'last_name', 'date_of_birth'])

    @extend_schema(
        responses={200: serializer_cls}
    )
    def get(self, request, user_id):
        user_full = UserFullInfo.objects.get(pk=user_id)

        body = self.serializer_cls(user_full).data
        return get_api_response(data=body)


class CurrentUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    serializer_cls = get_model_serializer(
        UserFullInfo,
        list_field=['id', 'email', 'first_name', 'last_name', 'date_of_birth'])

    @extend_schema(
        responses={200: serializer_cls}
    )
    def get(self, request):
        user_full = UserFullInfo.objects.get(user=request.user)

        body = self.serializer_cls(user_full).data
        return get_api_response(data=body)
