from django.db import models

# Testi alkaa

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    image = models.URLField(max_length=300, blank='True')
    released = models.IntegerField(blank='True')
    runtime = models.CharField(max_length=8, blank='True')
    imdb_id = models.CharField(max_length=10, default='', blank='True')
    imdb_rating = models.CharField(max_length=8, blank='True', default='')
    rotten_tomatoes_rating = models.CharField(max_length=4,  blank='True', default='')
    metacritic_rating = models.CharField(max_length=8,  blank='True', default='')

