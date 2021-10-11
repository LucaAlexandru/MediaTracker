from django.db import models
from django.contrib.auth.models import User
from MediaTracker.constants import RATING_TEN, FILM_TYPE
# Create your models here.


class Films(models.Model):
    film_name = models.CharField(max_length=100)
    film_release_date = models.DateField(null=True)
    film_genre = models.CharField(max_length=50)
    film_rating = models.CharField(max_length=10, choices=RATING_TEN, default="unrated")
    film_type = models.CharField(max_length=50, choices=FILM_TYPE, default="movie")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)