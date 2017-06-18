from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.user_roles.models.administrator import Administrator
from v1.user_roles.serializers.administrator import AdministratorSerializer


# administrators
class AdministratorView(APIView):

    @staticmethod
    def get(request):
        """
        List administrators
        """

        administrators = Administrator.objects.all()
        return Response(AdministratorSerializer(administrators, many=True).data)
