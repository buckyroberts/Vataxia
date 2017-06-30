from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.credits.models.transfer import Transfer
from v1.credits.models.wallet import Wallet


class TransferSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Transfer
        fields = '__all__'


class TransferSerializerCreate(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        """
        Validate sender balance
        """

        sender_wallet, _ = Wallet.objects.get_or_create(user=data.get('sender'))
        receiver_wallet, _ = Wallet.objects.get_or_create(user=data.get('receiver'))

        if data.get('amount') <= 0:
            raise serializers.ValidationError('Amount must be greater than zero')

        if data.get('amount') > sender_wallet.balance:
            raise serializers.ValidationError('Not enough credits')

        return data
