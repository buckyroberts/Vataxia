from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.replies.models.post_reply import PostReply
from v1.replies.serializers.post_reply import PostReplySerializer, PostReplySerializerCreate, PostReplySerializerUpdate


# post_replies
class PostReplyView(APIView):

    @staticmethod
    def post(request):
        """
        Create post reply
        """

        serializer = PostReplySerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostReplySerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# post_replies/{post_reply_id}
class PostReplyDetail(APIView):

    @staticmethod
    def patch(request, post_reply_id):
        """
        Update post reply
        """

        post_reply = get_object_or_404(PostReply, pk=post_reply_id)
        serializer = PostReplySerializerUpdate(post_reply, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(PostReplySerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, post_reply_id):
        """
        Delete post reply
        """

        post_reply = get_object_or_404(PostReply, pk=post_reply_id)
        if post_reply.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
