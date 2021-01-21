from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path("", views.game_main, name="game_main"),
    path("attack/", views.game_attack, name="game_attack"),
    path("list/", views.game_list, name="game_list"),
    path("list/<int:pk>/detail", views.game_detail, name="game_detail"),
    path("list/<int:pk>/counter", views.game_counter, name="game_counter"),
    path("list/<int:pk>/delete", views.game_counter, name="game_counter"),
]
