from django.db import models
from django.contrib.auth.models import User
from films.constants import FILM_RATING_TEN, FILM_TYPE
# Create your models here.


class Film(models.Model):
    film_name = models.CharField(max_length=100)
    film_release_date = models.DateField(null=True)
    film_genre = models.CharField(max_length=50, null=True)
    film_rating = models.CharField(max_length=10, choices=FILM_RATING_TEN, default="unrated")
    film_type = models.CharField(max_length=50, choices=FILM_TYPE, default="movie")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)