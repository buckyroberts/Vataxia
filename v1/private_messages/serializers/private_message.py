from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.private_messages.models.private_message import PrivateMessage


class PrivateMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = PrivateMessage
        fields = '__all__'


class PrivateMessageSerializerCreate(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PrivateMessage
        fields = '__all__'
