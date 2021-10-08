from django.contrib import admin
from games.models import Game

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ("game_name", "game_developer", "game_platform", "game_release_date",
                    "game_genre", "game_rating", "game_status")


admin.site.register(Game, GameAdmin)