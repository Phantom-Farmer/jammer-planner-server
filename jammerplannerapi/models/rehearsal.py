from django.db import models
from .user import User
from .band import Band
from .set import Set

class Rehearsal(models.Model):

    date = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    show = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
