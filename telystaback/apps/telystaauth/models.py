import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('必须拥有邮箱地址')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('超级用户必须设置 is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超级用户必须设置 is_superuser=True')

        return self._create_user(email, password, **extra_fields)




# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="用户uid")

    username = models.CharField(max_length=60,blank=False,verbose_name="用户名")

    email = models.EmailField(unique=True,blank=False,verbose_name="邮箱地址")

    telephone = models.CharField(max_length=20,blank=True,verbose_name="电话")

    date_joined = models.DateTimeField(auto_now_add=True,verbose_name="加入时间")

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

