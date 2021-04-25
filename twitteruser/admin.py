from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TwitterUser

class CustomUserAdmin(UserAdmin):
    model = TwitterUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('display_name', 'follow_users')}),
    )
# Register your models here.
admin.site.register(TwitterUser, CustomUserAdmin)
