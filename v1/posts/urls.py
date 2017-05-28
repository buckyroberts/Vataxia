from django.conf.urls import url
from .views.post import PostView, PostDetail


urlpatterns = [

    # Posts
    url(r'^posts$', PostView.as_view()),
    url(r'^posts/(?P<post_id>[\d]+)$', PostDetail.as_view()),

]
