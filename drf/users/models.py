import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.utils import timezone



class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        

        if not email:
            raise ValueError('No email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):
    username = None

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(
        max_length=12,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email
