from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse


class Game(models.Model):
    host = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="hosted_games"
    )
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="guested_games"
    )

    host_card = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ]
    )
    guest_card = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1),
        ],
    )

    is_end = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def is_host(self, user):
    #     return self.host == user

    def __str__(self):
        return f"{self.host.username} vs {self.guest.username}"

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
