from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.credits.models.invitation import Invitation
from v1.credits.models.wallet import Wallet


class InvitationSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Invitation
        fields = '__all__'


class InvitationSerializerCreate(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Invitation
        fields = ('sender',)

    def validate(self, data):
        """
        Validate that user has credit
        """

        wallet, _ = Wallet.objects.get_or_create(user=data.get('sender'))
        if wallet.balance < 1:
            raise serializers.ValidationError('Not enough credits')
        return data
