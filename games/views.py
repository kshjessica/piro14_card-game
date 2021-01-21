from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def game_main(request):
    return render(request, "games/game_main.html")


def game_attack(request):
    pass


def game_list(request):
    pass


def game_detail(request, pk):
    pass


def game_counter(request, pk):
    pass