from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Reply(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()

    class Meta:
        abstract = True
