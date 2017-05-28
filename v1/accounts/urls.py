from django.conf.urls import url
from .views.login import LoginView
from .views.logout import LogoutView
from .views.profile import ProfileView
from .views.user import UserView


urlpatterns = [

    # Login / logout
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),

    # Profiles
    url(r'^profiles$', ProfileView.as_view()),

    # Users
    url(r'^users$', UserView.as_view()),

]
