from django.conf.urls import url
from .views.administrator import AdministratorView
from .views.moderator import ModeratorView, ModeratorDetail


urlpatterns = [

    # Administrators
    url(r'^administrators$', AdministratorView.as_view()),

    # Moderators
    url(r'^moderators$', ModeratorView.as_view()),
    url(r'^moderators/(?P<moderator_id>[\d]+)$', ModeratorDetail.as_view()),

]
