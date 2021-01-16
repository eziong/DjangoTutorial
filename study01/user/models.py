import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pub_date = models.DateTimeField('date published',null=True)
    def __str__(self):
        return "username: " + self.username
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)