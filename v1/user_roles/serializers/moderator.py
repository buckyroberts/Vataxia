from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.user_roles.models.moderator import Moderator
from v1.utils import constants
from v1.utils.permissions import is_administrator, is_moderator


class ModeratorSerializer(serializers.ModelSerializer):
    sponsor = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Moderator
        fields = '__all__'


class ModeratorSerializerCreate(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Moderator
        fields = '__all__'

    def validate(self, data):
        """
        Administrator permissions needed
        """

        if not is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data

    def validate_user(self, user):
        """
        Ensure user is not already moderator or higher
        """

        if is_moderator(user):
            raise serializers.ValidationError('User already has moderator permissions')
        return user
