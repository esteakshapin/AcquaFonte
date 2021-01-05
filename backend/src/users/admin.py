# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email',
                    'first_name', 'last_name', 'avatar']
    ordering = ('email', 'first_name', 'last_name', 'avatar')
    # list_display = ('id', 'email',
    #                 'first_name', 'last_name', 'avatar')
    # ordering = ('email', 'password', 'first_name', 'last_name', 'avatar')
    fieldsets = (
        (None, {'fields': ('email',
                           'first_name', 'last_name', 'avatar',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',
                           'first_name', 'last_name', 'avatar')}),
    )


admin.site.register(User, CustomUserAdmin)
