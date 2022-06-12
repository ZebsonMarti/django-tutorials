from time import time
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Custom User Model.
    I want email to be used as username and the extra field are not required.
    """
    # User Manager
    objects = UserManager()

    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True
    )

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    # email and password will be required by default
    REQUIRED_FIELDS = []
