from django.contrib import admin
from .models.invitation import Invitation
from .models.transfer import Transfer
from .models.wallet import Wallet


admin.site.register(Invitation)
admin.site.register(Transfer)
admin.site.register(Wallet)
