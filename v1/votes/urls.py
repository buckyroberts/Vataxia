from django.conf.urls import url
from .views.post_vote import PostVoteView


urlpatterns = [

    # Post votes
    url(r'^post_votes$', PostVoteView.as_view()),

]
