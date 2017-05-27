from django.contrib import admin
from .models.profile import Profile
from .models.user import User


admin.site.register(Profile)
admin.site.register(User)
