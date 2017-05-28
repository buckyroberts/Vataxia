from rest_framework import serializers
from rest_framework.authtoken.models import Token
from v1.accounts.models.user import User


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'token')
