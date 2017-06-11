from rest_framework import serializers
from v1.accounts.models.profile import Profile
from v1.accounts.models.user import User
from .profile import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile')

    @staticmethod
    def get_profile(user):
        """
        Get or create profile 
        """

        profile, created = Profile.objects.get_or_create(user=user)
        return ProfileSerializer(profile, read_only=True).data


class UserSerializerCreate(UserSerializer):

    @staticmethod
    def validate_email(value):
        """
        Check the email is unique
        """

        if User.objects.filter(email=value):
            raise serializers.ValidationError('Email already exists')
        return value
