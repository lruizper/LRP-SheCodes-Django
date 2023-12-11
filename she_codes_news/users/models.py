from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    profile_pic = models.URLField(('profile-pic'), blank=True , null=True)
    # username = models.TextField(max_length=100 , blank=True , null=True)
    username = models.CharField(max_length=100, unique=True)
    about=models.TextField(blank=True)
    def __str__(self):
        return self.username