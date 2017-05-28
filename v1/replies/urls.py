from django.conf.urls import url
from .views.post_reply import PostReplyView


urlpatterns = [

    # Posts
    url(r'^post_replies$', PostReplyView.as_view()),

]
