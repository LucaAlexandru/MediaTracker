from django.contrib import admin
from books.models import Book


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "added_on", "published", "rating", "status", "genre")


admin.site.register(Book, BookAdmin)
