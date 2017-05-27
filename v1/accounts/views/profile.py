from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.models.profile import Profile
from v1.accounts.serializers.profile import ProfileSerializer


# profiles
class ProfileView(APIView):

    @staticmethod
    def get(request):
        """
        List profiles
        """

        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)
