from django.conf.urls import url
from .views.profile import ProfileView
from .views.user import UserView


urlpatterns = [

    # Profiles
    url(r'^profiles$', ProfileView.as_view()),

    # Users
    url(r'^users$', UserView.as_view()),

]
