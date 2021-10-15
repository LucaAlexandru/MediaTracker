from django.urls import path
from . import views

app_name = "films"

urlpatterns = [
    path('all/', views.films_data, name='all_films'),
    path('add_film/', views.add_film, name='add_film'),
    path('delete/<int:film_id>/', views.film_delete, name='film_delete'),
    path('functionality/<int:film_id>', views.film_functionality, name="film_functionality"),
    path('edit/<int:film_id>', views.film_edit, name="film_edit"),
    path('search_film/', views.search_film, name='film_search'),
    path('search_film_results/', views.search_film, name='film_results'),
    path('add_searched_film/', views.add_searched_film, name='add_searched_film'),
]