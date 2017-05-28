from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.posts.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def validate_user(self, user):
        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create posts for other users')
        return user
