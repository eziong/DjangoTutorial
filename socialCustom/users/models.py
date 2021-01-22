from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,user_name,first_name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email,user_name,first_name,password, **other_fields)
        
    def create_user(self,email,user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser1(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'),unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    account = models.CharField(max_length=100,blank=True)
    profit = models.IntegerField(default=0)
    asset = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name','username']

    def __str__(self):
        return 'self.start_date'

