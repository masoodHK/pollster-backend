from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField('Gender', max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    ban_status = models.BooleanField(default=False)