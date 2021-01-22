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
        host=request.user
        guest_name=request.POST.get('guest')
        host_card=request.POST.get('card_number')
        get_guest=User.objects.get(username=guest_name)
        game=Game(host=host, guest=get_guest, host_card=host_card)
        game.save()
        return redirect('games:game_detail', pk=game.pk)
    
    else:
        card_numbers = []
        while len(card_numbers) < 5:
            temp=random.randint(1, 10)
            if temp not in card_numbers:
                card_numbers.append(temp)
        guests=list(User.objects.all())
        guests.remove(request.user)
        ctx = {
            'guests': guests,
            'card_numbers': card_numbers,
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
    game=Game.objects.get(pk=pk)
    if request.method == "POST":
        guest_card=request.POST.get('card_number')
        game.guest_card=int(guest_card)
        """
        winner와 loser를 지정한다.
        무승부일 경우 winner와 loser에는 아무 값도 할당되지 않는다.
        무승부가 아닐 경우 winner.win과 loser.lose를 1 증가,
        무승부일 경우 host와 guest 모두의 win을 1 증가시킨다.
        """
        host_card, guest_card = game.host_card, game.guest_card

        if host_card != guest_card:  # 무승부가 아닐 때
            GM_UP, GM_DOWN = 0, 1
            gamemode = random.randint(0, 1)

            if gamemode == GM_UP:
                if host_card > guest_card:
                    game.winner = game.host
                    game.loser = game.guest
                else:
                    game.winner = game.guest
                    game.loser = game.host
            else:  # GM_DOWN
                if host_card < guest_card:
                    game.winner = game.host
                    game.loser = game.guest
                else:
                    game.winner = game.guest
                    game.loser = game.host

            game.winner.win += 1
            game.loser.lose += 1

        else:  # 무승부일 때
            game.host.win += 1
            game.guest.win += 1

        game.is_end = True
        game.save()
        return redirect('games:game_detail', pk=game.pk)
    
    else:
        card_numbers = []
        while len(card_numbers) < 5:
            temp=random.randint(1, 10)
            if temp not in card_numbers:
                card_numbers.append(temp)
        ctx = {
            'pk':pk,
            'card_numbers': card_numbers,
        }
        return render(request, "games/game_counter.html", ctx)


@login_required
def game_delete(request, pk):
    if request.method == "POST":
        game = get_object_or_404(Game, pk=pk)
        game.delete()
        return redirect("games:game_list")
    else:
        return redirect("games:game_list")
