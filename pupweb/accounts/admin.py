from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group

from .models import Subject, Grades, Department, Schedule
from .forms import UserAdmin

UserProfile = get_user_model()

# Register the new UserAdmin
admin.site.register(UserProfile, UserAdmin)

# Register your models here.
admin.site.register(Subject)
admin.site.register(Grades)
admin.site.register(Department)
admin.site.register(Schedule)

# If not using Django's built-in permissions, unregister Group model from admin.
# admin.site.unregister(Group)