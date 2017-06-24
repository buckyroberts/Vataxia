from django.conf.urls import url
from .views.private_message import PrivateMessageView, PrivateMessageDetail


urlpatterns = [

    # Private messages
    url(r'^private_messages$', PrivateMessageView.as_view()),
    url(r'^private_messages/(?P<private_message_id>[\d]+)$', PrivateMessageDetail.as_view()),

]
