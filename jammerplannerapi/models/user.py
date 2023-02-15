from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    image_url = models.URLField(max_length=250)
    email = models.EmailField(max_length=250)
