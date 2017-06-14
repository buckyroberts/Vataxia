from django.conf import settings
from django.db import models


class Profile(models.Model):
    image = models.ImageField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email
