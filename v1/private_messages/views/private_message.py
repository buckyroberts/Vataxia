from django.db.models import Q
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.private_messages.models.private_message import PrivateMessage
from v1.private_messages.serializers.private_message import PrivateMessageSerializer, PrivateMessageSerializerCreate


# private_messages
class PrivateMessageView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        """
        List private messages
        """

        private_messages = PrivateMessage.objects.filter(
            Q(receiver=request.user) |
            Q(sender=request.user)
        )
        return Response(PrivateMessageSerializer(private_messages, many=True).data)

    @staticmethod
    def post(request):
        """
        Create private message
        """

        serializer = PrivateMessageSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(PrivateMessageSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# private_messages/{private_message_id}
class PrivateMessageDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request, private_message_id):
        """
        View individual private message
        """

        private_message = PrivateMessage.objects.filter(
            Q(receiver=request.user) |
            Q(sender=request.user),
            pk=private_message_id
        ).first()
        if not private_message:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(PrivateMessageSerializer(private_message).data)
