from django.shortcuts import render
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
    pass


@login_required
def game_counter(request, pk):
    pass