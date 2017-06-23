from rest_framework import serializers
from rest_framework.authtoken.models import Token
from v1.accounts.models.profile import Profile
from v1.accounts.models.user import User
from v1.utils import constants
from v1.utils.permissions import is_administrator, is_moderator
from .profile import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'role')

    @staticmethod
    def get_profile(user):
        """
        Get or create profile
        """

        profile, created = Profile.objects.get_or_create(user=user)
        return ProfileSerializer(profile, read_only=True).data

    @staticmethod
    def get_role(user):
        """
        Get user role
        """

        if is_administrator(user):
            return constants.USER_ROLE_ADMINISTRATOR
        if is_moderator(user):
            return constants.USER_ROLE_MODERATOR


class UserSerializerCreate(UserSerializer):

    @staticmethod
    def validate_email(value):
        """
        Check the email is unique
        """

        if User.objects.filter(email=value):
            raise serializers.ValidationError('Email already exists')
        return value


class UserSerializerLogin(UserSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        """
        Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'role', 'token')


class UserSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
