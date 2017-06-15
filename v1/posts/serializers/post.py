from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.posts.models.post import Post
from v1.replies.serializers.post_reply import PostReplySerializer


class PostSerializer(serializers.ModelSerializer):
    post_replies = PostReplySerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def validate_user(self, user):
        """
        Validate authenticated user
        """

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create posts for other users')
        return user


class PostSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit posts from other users')
        return data
