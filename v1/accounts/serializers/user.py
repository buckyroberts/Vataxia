from rest_framework import serializers
from v1.accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
