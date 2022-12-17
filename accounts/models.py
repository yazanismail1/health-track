from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")


    def __str__(self):
        return self.username
