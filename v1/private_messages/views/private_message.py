from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.private_messages.models.private_message import PrivateMessage
from v1.private_messages.serializers.private_message import PrivateMessageSerializer


# private_messages
class PrivateMessageView(APIView):

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
