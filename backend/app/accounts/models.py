from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db.models import (
    CharField,
    DateTimeField,
    BooleanField,
)

from accounts.managers.objects import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    sub = CharField(
        max_length=256,
        default=uuid4,
        db_index=True,
        unique=True,
    )
    email = CharField(max_length=255, unique=True, blank=True, null=True)
    phone = CharField(max_length=20, unique=True, blank=True, null=True)
    first_name = CharField(max_length=256, blank=True, null=True)
    last_name = CharField(max_length=256, blank=True, null=True)
    date_joined = DateTimeField(default=timezone.now)
    is_staff = BooleanField(default=False)
    accept_agreement = BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def __str__(self):
        return self.email
