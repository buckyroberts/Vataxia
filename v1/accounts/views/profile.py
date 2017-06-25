from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.models.profile import Profile
from v1.accounts.serializers.profile import ProfileSerializer, ProfileSerializerUpdate
from v1.accounts.serializers.user import UserSerializerLogin


# profiles
class ProfileView(APIView):

    @staticmethod
    def get(request):
        """
        List profiles
        """

        profiles = Profile.objects.all()
        return Response(ProfileSerializer(profiles, many=True).data)


# profiles/{profile_id}
class ProfileDetail(APIView):

    @staticmethod
    def patch(request, profile_id):
        """
        Update profile of authenticated user
        """

        profile = get_object_or_404(Profile, pk=profile_id)
        if profile.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileSerializerUpdate(profile, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            profile = serializer.save()
            return Response(UserSerializerLogin(profile.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
