from django.contrib.auth.models import (AbstractUser, PermissionsMixin, BaseUserManager)
from django.core.validators import (MinValueValidator, MaxValueValidator)
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = False

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email address must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    DEFAULT_TIMEZONE = "UTC+4"

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25)
    password = models.CharField(max_length=256)
    username = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(unique=True)
    timezone = models.CharField(default=DEFAULT_TIMEZONE, max_length=10)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __repr__(self):
        return f"User({self.id})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
