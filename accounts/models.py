from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils import timezone


def upload_dir(instance, filename):
    return "{}/{}".format(instance.username, filename)

class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    bio = models.CharField(max_length=240, blank=True, default="")
    avatar = models.ImageField(upload_to=upload_dir, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):              # __unicode__ on Python 2
        return "@{}".format(self.username)

    def get_img_url(self, default_path="../img/icons/musicadence.jpg"):
        if self.image:
            return self.image
        return default_path

    def get_full_name(self):
        # The user is identified by their
        return self.username

    def get_short_name(self):
        # The user is identified by their
        return "{} ({})".format(self.username, self.email)
