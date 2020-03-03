from django.db import models

# Testi alkaa

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    image = models.URLField(max_length=200)
    released = models.IntegerField()
    runtime = models.CharField(max_length=8)
    imdb_id = models.CharField(max_length=150)
