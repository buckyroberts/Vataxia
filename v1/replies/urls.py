from django.conf.urls import url
from .views.post_reply import PostReplyView, PostReplyDetail


urlpatterns = [

    # Post replies
    url(r'^post_replies$', PostReplyView.as_view()),
    url(r'^post_replies/(?P<post_reply_id>[\d]+)$', PostReplyDetail.as_view()),

]
