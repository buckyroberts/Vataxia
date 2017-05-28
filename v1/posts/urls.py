from django.conf.urls import url
from .views.post import PostView


urlpatterns = [

    # Users
    url(r'^posts$', PostView.as_view()),

]
