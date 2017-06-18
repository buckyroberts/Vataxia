from rest_framework import serializers
from v1.votes.models.post_vote import PostVote


class PostVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostVote
        fields = '__all__'


class PostVoteSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostVote
        fields = '__all__'


class PostVoteSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = PostVote
        exclude = ('post', 'user')

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit post votes from other users')
        return data
