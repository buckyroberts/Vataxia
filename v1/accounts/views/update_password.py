from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.utils import constants


# update_password
class UpdatePasswordView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):
        """
        Update password for authenticated user
        """

        password = request.data.get('password')

        try:
            validate_password(password)
            request.user.set_password(password)
            request.user.save()
            return Response({constants.SUCCESS: 'Password has been updated'})
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({constants.ERROR: e}, status=status.HTTP_400_BAD_REQUEST)
