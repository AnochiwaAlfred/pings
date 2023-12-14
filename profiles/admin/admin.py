from django.contrib import admin
from profiles.models import *

# Register your models here.

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = FRIENDSHIP_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'Friendships'
        
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = USER_PROFILE_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'User Profiles'
        
@admin.register(UserSetting)
class UserSettingAdmin(admin.ModelAdmin):
    list_display = USER_SETTING_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'User Settings'
        
@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = USER_STATUS_LIST_DISPLAY

    class Meta:
        verbose_name_plural = 'User Statuses'