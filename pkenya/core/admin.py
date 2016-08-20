from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from pkenya.authentication.models import Profile
from .models import Page,FundRaisingPage,Events
class ProfileInline(admin.StackedInline):
    model=Profile
    list_display=('is_diplomat')
    can_delete=True
class UserAdmin(UserAdmin):
    list_display=('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    inlines=(ProfileInline,)
class PageAdmin(admin.ModelAdmin):
    list_display=('title','pub_date','was_published_recently')

admin.site.unregister(User)
admin.site.register(FundRaisingPage)
admin.site.register(Events)
admin.site.register(Page,PageAdmin)
admin.site.register(User,UserAdmin)
