from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from games.models import Game

# Create your views here.


def user_login(request):
    return render(request, "users/user_login.html")


@login_required
def user_ranking(request):
    users=User.objects.all()
    user_score=[]
    for i in users:
       score=[i.username,(i.win-i.lose)]
       user_score.append(score)
    for i in range(len(users)):
        for j in range(len(users)):
            if i < j:
                if user_score[i][1] < user_score[j][1]:
                    user_score[i],user_score[j] = user_score[j],user_score[i]

    ctx={'user_score':user_score, 'users':users}
    return render(request,"users/ranking.html",context=ctx)


def user_logout(request):
    if request.method == "POST":
        return redirect("games:game_main")
    if request.method == "GET":
        return render(request, "users/user_logout.html")
