from rest_framework.views import APIView
from api.common import get_api_response, get_model_serializer

from core.models import UserFullInfo


class UserProfileView(APIView):

    def get(self, request, user_id):
        user_full = UserFullInfo.objects.get(pk=user_id)

        serializer_cls = get_model_serializer(
            UserFullInfo,
            list_field=['id', 'email', 'first_name', 'last_name'])

        body = serializer_cls(user_full).data
        return get_api_response(data=body)
