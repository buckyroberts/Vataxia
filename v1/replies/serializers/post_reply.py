from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.replies.models.post_reply import PostReply


class PostReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostReply
        fields = '__all__'
