from django.contrib import admin
from .models.administrator import Administrator
from .models.moderator import Moderator


admin.site.register(Administrator)
admin.site.register(Moderator)
