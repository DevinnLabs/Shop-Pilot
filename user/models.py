from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager

# Create your models here.

# Role Enum
class Role(models.TextChoices):
    SUPER_USER = 'super_user'
    ADMIN = 'admin'
    USER = 'user'

# User Model
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(("email"), unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(
        max_length=20,
        default=Role.USER.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name