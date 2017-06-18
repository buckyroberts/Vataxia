from django.db import models
from v1.posts.models.post import Post
from v1.votes.models.vote import Vote


class PostVote(Vote):
    post = models.ForeignKey(Post)

    class Meta:
        default_related_name = 'post_votes'
        unique_together = ('post', 'user')

    def __str__(self):
        return f'post: {self.post.id} - value: {self.value}'
