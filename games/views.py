from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from games.models import Game
from games.forms import GameForm
from django.contrib.auth.decorators import login_required


def games_data(request):
    data = Game.objects.all().order_by('game_name')
    return render(request, 'games/all_games.html', {"games_data_1": data})


@login_required(login_url="/accounts/login/")
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('games:all_games')
        else:
            return HttpResponseRedirect('not valid')
    else:
        form = GameForm()
    return render(request, 'books/add_book.html', {'book_form': form})


def game_delete(request, game_id):
    game = Game.objects.get(pk=game_id)
    game.delete()
    return redirect("games:all_games")
