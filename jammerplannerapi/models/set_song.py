from django.db import models
from .set import Set
from .song import Song
from .band import Band

class Set_Song(models.Model):

    set = models.ForeignKey(Set, related_name="set_songs", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="set_songs",on_delete=models.CASCADE)
    order = models.CharField(max_length=50)
