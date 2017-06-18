from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Administrator(CreatedModified):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email
