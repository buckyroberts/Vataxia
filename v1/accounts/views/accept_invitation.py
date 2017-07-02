from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.serializers.accept_invitation import AcceptInvitationSerializer
from v1.accounts.serializers.user import UserSerializerLogin


# accept_invitation
class AcceptInvitationView(APIView):
    authentication_classes = ()
    permission_classes = ()

    @staticmethod
    def post(request):
        """
        Accept invitation and create user
        """

        serializer = AcceptInvitationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializerLogin(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
