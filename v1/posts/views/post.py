from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.filters.posts.post import post_filter
from v1.posts.models.post import Post
from v1.posts.serializers.post import PostSerializer, PostSerializerCreate, PostSerializerFull, PostSerializerUpdate


# posts
class PostView(APIView):

    @staticmethod
    def get(request):
        """
        List posts
        """

        posts = Post.objects.all()
        posts = post_filter(request, posts)
        if type(posts) == Response:
            return posts
        return Response(PostSerializer(posts, many=True).data)

    @staticmethod
    def post(request):
        """
        Create post
        """

        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# posts/{post_id}
class PostDetail(APIView):

    @staticmethod
    def get(request, post_id):
        """
        View individual post
        """

        post = get_object_or_404(Post, pk=post_id)
        return Response(PostSerializerFull(post).data)

    @staticmethod
    def patch(request, post_id):
        """
        Update post
        """

        post = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializerUpdate(post, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializerFull(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, post_id):
        """
        Delete post
        """

        post = get_object_or_404(Post, pk=post_id)
        if post.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
