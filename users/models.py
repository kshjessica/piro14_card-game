from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    win = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)