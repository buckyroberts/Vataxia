from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
