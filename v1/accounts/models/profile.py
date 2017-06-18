from django.conf import settings
from django.db import models


class Profile(models.Model):
    image = models.ImageField(blank=True)
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='sponsored_users')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email
