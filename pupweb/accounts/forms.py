from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

UserProfile = get_user_model()

class RegisterForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """

    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'mobile_num', 'branch', 'is_regular']

    def clean_email(self):
        """
        Verify email is available.
        """

        email = self.cleaned_data.get('email')
        qs = UserProfile.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is already taken.')
        
        return email

    def clean(self):
        """
        Verify both passwords match.
        """

        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password_2', 'The passwords do not match.')
        
        return cleaned_data


class UserAdminCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """

    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'mobile_num', 'branch', 'is_regular']

    def clean_email(self):
        """
        Verify email is available.
        """

        email = self.cleaned_data.get('email')
        qs = UserProfile.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is already taken.')
        
        return email

    def clean(self):
        """
        Verify both passwords match.
        """

        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password_2', 'The passwords do not match.')
        
        return cleaned_data


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'mobile_num', 'branch', 'is_regular', 'admin', 'is_active']

    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value.

        This is done here, rather than on the field, because the field does not have access to the initial value
        """
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    # The form to add and change user instance
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    """
    The fields to be used in displaying the UserProfile model.
    
    These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    """

    list_display = ['user_id', 'first_name', 'middle_name', 'last_name', 'email', 'address', 'sex', 'birthday', 'age', 'branch', 'is_regular', 'password', 'is_active', 'admin', 'staff']
    list_filter = ['admin', 'sex', 'branch']
    fieldsets = (
        (None, {'fields': ('user_id', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'address', 'sex', 'birthday', 'branch', 'is_regular',)}),
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
    search_fields = ['user_id', 'first_name', 'middle_name', 'last_name', 'email']
    ordering = ['user_id']
    filter_horizontal = ()



