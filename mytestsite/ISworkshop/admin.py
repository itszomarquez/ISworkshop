from django.contrib import admin
from .models import ProfilePage
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#class ProfilePageAdmin(UserAdmin):
#    list_display=('first_name', 'last_name')


admin.site.register(ProfilePage)
#, ProfilePageAdmin)
