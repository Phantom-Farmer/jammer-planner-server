from django.db import models
from .user import User
from .band import Band

class Set(models.Model):

    title = models.CharField(max_length=50)
    song = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
