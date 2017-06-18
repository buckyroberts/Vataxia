from rest_framework import serializers
from rest_framework.authtoken.models import Token
from v1.accounts.models.profile import Profile
from v1.accounts.models.user import User
from .profile import ProfileSerializer


class LoginSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_profile(user):
        """
        Get or create profile
        """

        profile, created = Profile.objects.get_or_create(user=user)
        return ProfileSerializer(profile, read_only=True).data

    @staticmethod
    def get_token(user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile', 'token')
