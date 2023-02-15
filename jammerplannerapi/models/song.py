from django.db import models
from .user import User
from .band import Band

class Song(models.Model):

    title = models.CharField(max_length=50)
    key = models.CharField(max_length=20)
    signature = models.CharField(max_length=20)
    vibe = models.CharField(max_length=250)
    lyric = models.CharField(max_length=1000)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
