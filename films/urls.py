from django.urls import path
from . import views

app_name = "films"

urlpatterns = [
    path('all/', views.films_data, name='all_films'),
    path('add_film/', views.add_film, name='add_film'),
    path('delete/<int:film_id>/', views.film_delete, name='film_delete')
]