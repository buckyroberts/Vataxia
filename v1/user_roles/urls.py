from django.conf.urls import url
from .views.administrator import AdministratorView


urlpatterns = [

    # Administrators
    url(r'^administrators$', AdministratorView.as_view()),

]
