from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.votes.models.post_vote import PostVote
from v1.votes.serializers.post_vote import PostVoteSerializer, PostVoteSerializerCreate, PostVoteSerializerUpdate


# post_votes
class PostVoteView(APIView):

    @staticmethod
    def post(request):
        """
        Create post vote
        """

        serializer = PostVoteSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostVoteSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
