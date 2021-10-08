from django import forms
from MediaTracker.constants import STATUS_CHOICES, GENRE_CHOICES

book_rating = (
    ("0", "unrated"), ("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"), ("5", "five")
)


class BookForm(forms.Form):
    new_name = forms.CharField(label="Book name", max_length=50)
    new_author = forms.CharField(label="Author", max_length=50)
    new_added_on = forms.DateField(label="Added on")
    new_published = forms.DateField(label="Published")
    new_rating = forms.ChoiceField(label="Rating", choices=book_rating)
    new_status = forms.ChoiceField(choices=STATUS_CHOICES)
    new_genre = forms.ChoiceField(choices=GENRE_CHOICES)
