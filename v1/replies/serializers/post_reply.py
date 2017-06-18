from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.replies.models.post_reply import PostReply


class PostReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostReply
        fields = '__all__'


class PostReplySerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = PostReply
        fields = '__all__'

    def validate_user(self, user):
        """
        Validate authenticated user
        """

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create post replies for other users')
        return user


class PostReplySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = PostReply
        exclude = ('post', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit post replies from other users')
        return data
