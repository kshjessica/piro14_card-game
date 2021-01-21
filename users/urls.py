from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("ranking/", views.user_ranking, name="user_ranking"),
    path("logout/", views.user_logout, name="user_logout"),
]
