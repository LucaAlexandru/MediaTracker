from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('all/', views.games_data, name='all_games'),
    path('add_game/', views.add_game, name='add_game'),
    path('delete/<int:game_id>/', views.game_delete, name='game_delete'),
    path('functionality/<int:game_id>', views.functionality, name="functionality")
]