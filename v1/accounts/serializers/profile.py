from rest_framework import serializers
from v1.accounts.models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('image',)
