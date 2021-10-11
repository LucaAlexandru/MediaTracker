from films.models import Film
from django import forms


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        exclude = ('user',)
