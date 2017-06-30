from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.credits.models.invitation import Invitation
from v1.credits.serializers.invitation import InvitationSerializer, InvitationSerializerCreate
from v1.credits.models.wallet import Wallet
from v1.filters.credits.invitation import invitation_filter


# invitations
class InvitationView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        """
        List invitations
        """

        invitations = Invitation.objects.all()
        invitations = invitation_filter(request, invitations)
        if type(invitations) == Response:
            return invitations
        return Response(InvitationSerializer(invitations, many=True).data)

    @staticmethod
    def post(request):
        """
        Create invitation
        """

        serializer = InvitationSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            wallet, _ = Wallet.objects.get_or_create(user=request.user)
            wallet.balance -= 1
            wallet.save()
            return Response(InvitationSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
