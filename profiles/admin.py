from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'get_address',
        'get_city'
    )
    list_select_related = ('profile',)

    def get_address(self, instance):
        return instance.profile.address
    get_address.short_description = 'Address'

    def get_city(self, instance):
        return instance.profile.city
    get_city.short_description = 'City'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
