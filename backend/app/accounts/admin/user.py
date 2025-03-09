from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .base import admin
from accounts import models
from .base import AdminUpdatedFields


class UserDash(UserAdmin, AdminUpdatedFields):
    list_display = (
        "email",
        "phone",
    )
    list_display_links = (
        "email",
        "phone",
    )
    readonly_fields = ["sub", "email", "phone", "last_login", "date_joined"]
    search_fields = ("email", "phone", "sub")
    ordering = ("-last_login",)
    list_filter = ("is_staff", "groups")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "phone", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (
            _("Personal info"),
            {
                "fields": (
                    "sub",
                    "email",
                    "phone",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "accept_agreement",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            _("Business"),
            {
                "fields": (
                    # "get_companies",
                ),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.is_staff:
            readonly_fields = ["is_staff", "is_superuser", "groups", "user_permissions"]
            readonly_fields.extend(self.readonly_fields)
            return readonly_fields
        return self.readonly_fields


admin.site.register(models.User, UserDash)
