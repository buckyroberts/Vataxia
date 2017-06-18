from django.conf.urls import url
from .views.post_vote import PostVoteView, PostVoteDetail


urlpatterns = [

    # Post votes
    url(r'^post_votes$', PostVoteView.as_view()),
    url(r'^post_votes/(?P<post_vote_id>[\d]+)$', PostVoteDetail.as_view()),

]
