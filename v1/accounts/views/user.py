from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.serializers.user import UserSerializer


# users
class UserView(APIView):

    @staticmethod
    def get(request):
        """
        List users
        """

        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)
