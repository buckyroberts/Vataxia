from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class PrivateMessage(CreatedModified):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver')
    body = models.TextField()

    class Meta:
        default_related_name = 'private_messages'

    def __str__(self):
        return self.body
