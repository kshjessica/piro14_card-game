from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    return render(request, "users/user_login.html")


@login_required
def user_ranking(request):
    pass


def user_logout(request):
    if request.method == "POST":
        return redirect("games:game_main")
    if request.method == "GET":
        return render(request, "users/user_logout.html")
