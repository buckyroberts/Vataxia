from rest_framework import serializers
from v1.accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserSerializerCreate(UserSerializer):

    @staticmethod
    def validate_email(value):
        """
        Check the email is unique
        """

        if User.objects.filter(email=value):
            raise serializers.ValidationError('Email already exists')
        return value
