from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True, blank = True)
    invited_by = models.CharField(max_length = 200, null = False, default = 'faxriyor')