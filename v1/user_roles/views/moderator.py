from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.user_roles.models.moderator import Moderator
from v1.user_roles.serializers.moderator import ModeratorSerializer, ModeratorSerializerCreate
from v1.utils import constants
from v1.utils.permissions import is_administrator


# moderators
class ModeratorView(APIView):

    @staticmethod
    def get(request):
        """
        List moderators
        """

        moderators = Moderator.objects.all()
        return Response(ModeratorSerializer(moderators, many=True).data)

    @staticmethod
    def post(request):
        """
        Create moderator
        """

        serializer = ModeratorSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(ModeratorSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# moderators/{moderator_id}
class ModeratorDetail(APIView):

    @staticmethod
    def delete(request, moderator_id):
        """
        Delete moderator
        """

        moderator = get_object_or_404(Moderator, pk=moderator_id)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_403_FORBIDDEN)
        moderator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
