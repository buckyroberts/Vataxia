from django.conf.urls import url
from .views.private_message import PrivateMessageView


urlpatterns = [

    # Private messages
    url(r'^private_messages$', PrivateMessageView.as_view()),

]
