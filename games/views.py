from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from random import shuffle
from .models import Game
from users.models import User


def game_main(request):
    return render(request, "games/game_main.html")


@login_required
def game_attack(request):
    if request.method == "POST":
        pass
    else:
        card_numbers = list(range(1, 11))
        print(card_numbers)
        ctx = {
            "users": User.objects.all(),
            "card_numbers": card_numbers,
        }
        return render(request, "games/game_attack.html", ctx)


@login_required
def game_list(request):
    return render(request, "games/game_list.html")


@login_required
def game_detail(request, pk):
    ctx = {
        "game": get_object_or_404(Game, pk=pk),
    }
    return render(request, "games/game_detail.html", ctx)


@login_required
def game_counter(request, pk):
    pass


@login_required
def game_delete(request, pk):
    if request.method == "POST":
        game = get_object_or_404(Game, pk=pk)
        game.delete()
        return redirect("games:game_list")
    else:
        return redirect("games:game_list")
