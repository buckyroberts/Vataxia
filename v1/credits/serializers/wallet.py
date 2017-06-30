from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.credits.models.wallet import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Wallet
        fields = '__all__'
