from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Transfer(CreatedModified):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_transfers')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_transfers')
    amount = models.IntegerField()

    class Meta:
        default_related_name = 'transfers'

    def __str__(self):
        return f'{self.sender.email} > {self.receiver.email} - {self.amount}'
