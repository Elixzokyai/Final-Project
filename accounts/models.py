from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BlogUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)

