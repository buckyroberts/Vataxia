from rest_framework.response import Response
from rest_framework.views import APIView
from v1.posts.models.post import Post
from v1.posts.serializers.post import PostSerializer


# posts
class PostView(APIView):

    @staticmethod
    def get(request):
        """
        List posts
        """

        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)
