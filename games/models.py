from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from random import shuffle

CARD_MAX = 5


class Game(models.Model):
    host = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="hosted_games"
    )
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="guested_games"
    )

    CARD_SELECT = list(range(1, 11))
    shuffle(CARD_SELECT)
    CARD_SELECT = sorted(CARD_SELECT[:CARD_MAX])
    for i in range(CARD_MAX):
        CARD_SELECT[i] = (CARD_SELECT[i], CARD_SELECT[i])

    host_card = models.PositiveIntegerField(
        choices=CARD_SELECT,
        default=CARD_SELECT[0],
    )
    guest_card = models.PositiveIntegerField(
        choices=CARD_SELECT,
        default=CARD_SELECT[0],
    )

    is_end = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
