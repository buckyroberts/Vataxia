from django.conf import settings
from django.db import models
from v1.utils import constants


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    value = models.IntegerField(choices=constants.VOTE_VALUE_CHOICES)

    class Meta:
        abstract = True
