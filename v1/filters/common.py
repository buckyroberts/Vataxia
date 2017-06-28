from rest_framework import status
from rest_framework.response import Response
from v1.utils import constants


def filter_query_params(allowed, query, request):
    """
    Filter request query parameters
    """

    kwargs = {}
    for param in allowed.keys() & request.query_params.keys():
        try:
            kwargs[param] = allowed[param](request.query_params[param])
        except Exception as e:
            return Response({constants.ERROR: {param: str(e)}}, status=status.HTTP_400_BAD_REQUEST)
    return query.filter(**kwargs)
