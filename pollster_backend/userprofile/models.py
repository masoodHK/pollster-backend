from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    class Meta:
        verbose_name_plural = "User Profile"

    gender = models.CharField('Gender', max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    ban_status = models.BooleanField(default=False)
    profile_pic_url = models.TextField("Your profile picture", null=True, max_length=1000)
    