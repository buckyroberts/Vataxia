from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Post(CreatedModified):
    body = models.TextField()
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.body
