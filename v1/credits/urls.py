from django.conf.urls import url
from .views.invitation import InvitationView
from .views.transfer import TransferView
from .views.wallet import WalletDetail


urlpatterns = [

    # Invitations
    url(r'^invitations$', InvitationView.as_view()),

    # Transfers
    url(r'^transfers$', TransferView.as_view()),

    # Wallets
    url(r'^wallets/(?P<user_id>[\d]+)$', WalletDetail.as_view()),

]
