from django.conf import settings
from django.db import models


class Wallet(models.Model):
    balance = models.IntegerField(default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email
