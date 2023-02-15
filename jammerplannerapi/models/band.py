from django.db import models
from .user import User


class Band(models.Model):

    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
