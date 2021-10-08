from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('all/', views.games_data, name='all_games'),
    path('add_book/', views.add_game, name='add_game'),
    path('delete/<int:book_id>/', views.game_delete, name='game_delete')
]