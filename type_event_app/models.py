from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser, BaseUserManager):
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.username
