from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.accounts.models.profile import Profile
from v1.accounts.models.user import User
from v1.accounts.serializers.user import UserSerializer, UserSerializerCreate, UserSerializerLogin, UserSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_administrator, is_moderator


# users
class UserView(APIView):

    @staticmethod
    def get(request):
        """
        List users
        """

        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

    @staticmethod
    def post(request):
        """
        Create user
        """

        serializer = UserSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            Profile(user=user).save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# users/{user_id}
class UserDetail(APIView):

    @staticmethod
    def get(request, user_id):
        """
        View individual user
        """

        user = get_object_or_404(User, pk=user_id)
        return Response(UserSerializer(user).data)

    @staticmethod
    def patch(request, user_id):
        """
        Update authenticated user
        """

        user = get_object_or_404(User, pk=user_id)
        if user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializerUpdate(user, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializerLogin(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, user_id):
        """
        Delete user
        """

        user = get_object_or_404(User, pk=user_id)
        if is_administrator(user) or user.is_superuser:
            return Response({
                constants.ERROR: 'That user can not be deleted'
            }, status=status.HTTP_401_UNAUTHORIZED)
        if is_moderator(user) and not is_administrator(request.user):
            return Response({
                constants.ERROR: 'Admin permissions needed to delete moderators'
            }, status=status.HTTP_401_UNAUTHORIZED)
        if not is_moderator(request.user):
            return Response({
                constants.ERROR: 'Moderator permissions needed to delete users'
            }, status=status.HTTP_401_UNAUTHORIZED)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
