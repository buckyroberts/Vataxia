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


# post_votes/{post_vote_id}
class PostVoteDetail(APIView):

    @staticmethod
    def patch(request, post_vote_id):
        """
        Update post vote
        """

        post_vote = get_object_or_404(PostVote, pk=post_vote_id)
        serializer = PostVoteSerializerUpdate(post_vote, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(PostVoteSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, post_vote_id):
        """
        Delete post vote
        """

        post_vote = get_object_or_404(PostVote, pk=post_vote_id)
        if post_vote.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post_vote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
