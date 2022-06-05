from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

from mysite.models.abstract import TimeStampMixin


class CusUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
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
            password=password
        )
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # for use admin site
    is_admin = models.BooleanField(default=False)

    objects = CusUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    # below code for use admin site
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserProfileAbs(TimeStampMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        parent_link=False,
        primary_key=True,
    )
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    class Meta:
        abstract = True


class UserProfile(UserProfileAbs):
    class Meta:
        db_table = 'user_profile'


class UserFullInfo(User, UserProfileAbs):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    profile_created_at = models.DateTimeField(auto_now_add=True,
                                              db_column='created_at')
    profile_updated_at = models.DateTimeField(auto_now=True,
                                              db_column='updated_at')

    class Meta:
        managed = False
        db_table = 'user_profile'
