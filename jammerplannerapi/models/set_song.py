from django.db import models
from .set import Set
from .song import Song

class Set_Song(models.Model):

    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)