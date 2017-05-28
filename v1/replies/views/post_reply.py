from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.replies.serializers.post_reply import PostReplySerializer, PostReplySerializerCreate


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
