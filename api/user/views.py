from rest_framework.views import APIView,Response


class UserProfile(APIView):

	def get(self, request):
		return Response(data={"result": "OK"})
