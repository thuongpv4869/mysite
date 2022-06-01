from rest_framework import status, serializers
from rest_framework.response import Response


class ApiResponseBody():
    def __init__(self, data, error=None) -> None:
        self.data = data
        self.error = error
        self.result = 'success' if not error else 'failure'

    def json(self):
        return {
            "result": self.result,
            "data": self.data,
            "error": self.error
        }


def get_api_response(data, error=None, status=status.HTTP_200_OK):
    body = ApiResponseBody(data, error).json()
    return Response(data=body, status=status)


def get_model_serializer(model_cls, list_field: list):

    class Cls(serializers.ModelSerializer):
        class Meta:
            nonlocal model_cls, list_field
            model = model_cls
            fields = list_field

    return Cls
