from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.posts.models.post import Post
from v1.posts.serializers.post import PostSerializer, PostSerializerCreate


# posts
class PostView(APIView):

    @staticmethod
    def get(request):
        """
        List posts
        """

        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)

    @staticmethod
    def post(request):
        """
        Create post
        """

        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
