from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.models.user import User
from v1.credits.models.wallet import Wallet
from v1.credits.serializers.wallet import WalletSerializer


# wallets/{user_id}
class WalletDetail(APIView):

    @staticmethod
    def get(request, user_id):
        """
        View individual wallet
        """

        user = get_object_or_404(User, pk=user_id)
        wallet, _ = Wallet.objects.get_or_create(user=user)
        return Response(WalletSerializer(wallet).data)
