from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from books.models import Book
from books.forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def books_data(request):
    data = Book.objects.all().order_by('status')
    return render(request, 'books/all_books.html', {"books_data_1": data})


@login_required(login_url="/accounts/login/")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            cleaned_name = form.cleaned_data.get('new_name')
            cleaned_author = form.cleaned_data.get('new_author')
            cleaned_added_on = form.cleaned_data.get('new_added_on')
            cleaned_published = form.cleaned_data.get('new_published')
            cleaned_rating = form.cleaned_data.get('new_rating')
            cleaned_status = form.cleaned_data.get('new_status')
            cleaned_genre = form.cleaned_data.get('new_genre')
            new_book = Book(name=cleaned_name, author=cleaned_author, added_on=cleaned_added_on,
                            published=cleaned_published, rating=cleaned_rating,
                            status=cleaned_status, genre=cleaned_genre)
            new_book.save()
            # new_book.save(commit=False)
            # book.user = request.user
            return redirect('books:all_books')
        else:
            return HttpResponseRedirect('not valid')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'book_form': form})


def book_delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("books:all_books")
