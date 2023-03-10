from django.db import models
from .user import User
from .band import Band

class Set(models.Model):

    title = models.CharField(max_length=50)
    note = models.CharField(max_length=1000)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def songs(self):
        set_songs = self.set_songs.all()
        return [set_song.song for set_song in set_songs]
