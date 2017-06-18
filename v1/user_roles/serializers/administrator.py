from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.user_roles.models.administrator import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        fields = '__all__'
