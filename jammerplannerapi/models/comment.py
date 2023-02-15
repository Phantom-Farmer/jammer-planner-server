from django.db import models
from .user import User
from .rehearsal import Rehearsal

class Comment(models.Model):

    content = models.CharField(max_length=500)
    rehearsal = models.ForeignKey(Rehearsal, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
