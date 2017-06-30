from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.credits.models.transfer import Transfer
from v1.credits.models.wallet import Wallet
from v1.credits.serializers.transfer import TransferSerializer, TransferSerializerCreate
from v1.filters.credits.transfer import transfer_filter


# transfers
class TransferView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        """
        List transfers
        """

        transfers = Transfer.objects.all()
        transfers = transfer_filter(request, transfers)
        if type(transfers) == Response:
            return transfers
        return Response(TransferSerializer(transfers, many=True).data)

    @staticmethod
    def post(request):
        """
        Create transfer
        """

        serializer = TransferSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            transfer = serializer.save()
            sender_wallet, _ = Wallet.objects.get_or_create(user=transfer.sender)
            receiver_wallet, _ = Wallet.objects.get_or_create(user=transfer.receiver)
            sender_wallet.balance -= transfer.amount
            receiver_wallet.balance += transfer.amount
            sender_wallet.save()
            receiver_wallet.save()
            return Response(TransferSerializer(transfer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
