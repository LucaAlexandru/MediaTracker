from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from films.models import Film
from films.forms import FilmForm
from django.contrib.auth.decorators import login_required


def films_data(request):
    data = Film.objects.all().order_by('film_name')
    return render(request, 'films/all_films.html', {"films_data_1": data})


@login_required(login_url="/accounts/login/")
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:all_films')
        else:
            return HttpResponseRedirect('not valid')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'film_form': form})


@login_required(login_url="/accounts/login/")
def film_delete(request, film_id):
    film = Film.objects.get(pk=film_id)
    film.delete()
    return redirect("films:all_films")


@login_required(login_url="/accounts/login/")
def film_functionality(request, film_id):
    film = Film.objects.get(pk=film_id)
    return render(request, 'films/functionality.html', {"film_data_2": film})


@login_required(login_url="/accounts/login/")
def film_edit(request, film_id):
    film = Film.objects.get(pk=film_id)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect("films:all_films")
        else:
            return HttpResponseRedirect("Not valid, please try again.")
    else:
        form = FilmForm(instance=film)
    return render(request, 'films/edit_film.html', {'edit_form': form})
