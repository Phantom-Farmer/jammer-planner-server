from django.db import models
from .set import Set
from .song import Song
from .band import Band

class Set_Song(models.Model):

    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.CharField(max_length=50)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
