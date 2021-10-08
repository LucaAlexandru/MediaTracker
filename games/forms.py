from django import forms
from games.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        exclude = ('user',)