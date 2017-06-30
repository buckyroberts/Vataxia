from v1.filters.common import filter_query_params


def invitation_filter(request, query):
    """
    Filter results based on request query parameters
    """

    allowed = {
        'sender': lambda x: int(x),
    }

    return filter_query_params(allowed, query, request)
