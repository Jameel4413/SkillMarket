from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # 'username' ki jagah 'email' se sorting set kar rahe hain
    ordering = ('email',)

    # Admin panel ki list view mein ye fields nazar aayengi
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # Search bar mein email, first_name aur last_name se search ho sakega
    search_fields = ('email', 'first_name', 'last_name')

    # Admin panel par edit Form Layout
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Naya User create karte waqt ka form configuration
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )