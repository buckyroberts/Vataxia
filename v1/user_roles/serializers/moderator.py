from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.user_roles.models.moderator import Moderator


class ModeratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Moderator
        fields = '__all__'
