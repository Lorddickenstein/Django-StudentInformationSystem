from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

UserProfile = get_user_model()

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The form to add and change user instance
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    """
    The fields to be used in displaying the UserProfile model.
    
    These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    """

    list_display = ['user_id', 'first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'age', 'branch', 'is_regular', 'password', 'is_active', 'admin', 'staff']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('user_id', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name,', 'address', 'sex', 'birthday', 'branch', 'is_regular',)}),
        ('Permission', {'fields': ('admin',)}),
    )
    """
    add_fieldsets is not a standard ModelAdmin attribute. UserAdmin overrides get_fieldsets to use this attribute when creating a user.
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'branch', 'password', 'password_2')
        }),
    )
    search_fields = ['user_id']
    ordering = ['user_id']
    filter_horizontal = ()


# Register the new UserAdmin
admin.site.register(UserProfile, UserAdmin)

# If not using Django's built-in permissions, unregister Group model from admin.
# admin.site.unregister(Group)