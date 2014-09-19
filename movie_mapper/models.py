from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=120)
    movie_id = models.CharField(unique=True, max_length=10)
    searched = models.BooleanField(default=False)
    user = models.ManyToManyField(User, related_name='movies')

    def __unicode__(self):
        return u"{}".format(self.title)


class Location(models.Model):
    place = models.CharField(unique=True, max_length=120)
    searched = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie, related_name='locations')
    user = models.ManyToManyField(User, related_name='locations')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __unicode__(self):
        return u"{}".format(self.place)