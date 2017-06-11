from django.contrib import admin
from .models.profile import Profile
from .models.user import User


class UserAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')

admin.site.register(Profile)
admin.site.register(User, UserAdmin)
