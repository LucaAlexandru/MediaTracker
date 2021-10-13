from django.db import models
from django.contrib.auth.models import User
from books.constants import BOOK_STATUS_CHOICES, BOOK_GENRE_CHOICES


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    added_on = models.DateField(null=True)
    published = models.DateField(null=True)

    class Rating(models.IntegerChoices):
        unrated = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    rating = models.IntegerField(choices=Rating.choices, null=True)
    status = models.CharField(max_length=30, choices=BOOK_STATUS_CHOICES, default="read")
    genre = models.CharField(max_length=40, choices=BOOK_GENRE_CHOICES, default="other")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
