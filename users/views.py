from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    pass


@login_required
def user_ranking(request):
    pass


def user_logout(request):
    pass