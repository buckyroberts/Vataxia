from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Post(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True)

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.title
