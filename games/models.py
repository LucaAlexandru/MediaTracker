from django.db import models
from django.contrib.auth.models import User
from MediaTracker.constants import RATING, GAME_STATUS_CHOICES, GAME_PLATFORM


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_developer = models.CharField(max_length=100)
    game_platform = models.CharField(max_length=50, choices=GAME_PLATFORM, default="pc")
    game_release_date = models.DateField(null=True)
    game_genre = models.CharField(max_length=50)
    game_rating = models.CharField(max_length=40, choices=RATING, default="unrated")
    game_status = models.CharField(max_length=50, choices=GAME_STATUS_CHOICES, default="unplayed")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)