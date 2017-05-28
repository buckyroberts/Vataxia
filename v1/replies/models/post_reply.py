from django.db import models
from v1.posts.models.post import Post
from .reply import Reply


class PostReply(Reply):
    post = models.ForeignKey(Post)

    class Meta:
        default_related_name = 'post_replies'

    def __str__(self):
        return self.body
