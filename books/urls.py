from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('all/', views.books_data, name='all_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete/<int:book_id>/', views.book_delete, name='book_delete')
]