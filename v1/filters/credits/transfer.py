from v1.filters.common import filter_query_params


def transfer_filter(request, query):
    """
    Filter results based on request query parameters
    """

    allowed = {
        'receiver': lambda x: int(x),
        'sender': lambda x: int(x),
    }

    return filter_query_params(allowed, query, request)
