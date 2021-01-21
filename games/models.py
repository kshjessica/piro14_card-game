from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse


class Game(models.Model):
    """ Game Model Class """

    # host는 게임을 시작한(공격한)유저이다.
    # guest는 게임을 받은(공격 받은)유저이다.
    # 이 둘은 게임이 만들어질 때 game_attack 뷰에서 입력받는다.
    host = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="hosted_games"
    )
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="guested_games"
    )

    # host와 guest의 카드 숫자를 저장하는 필드이다.
    # 게임이 만들어질때 game_attack 뷰에서는 host_card만 입력받고
    # guest_card는 기본값 0을 넣어둔다.
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

    # 게임이 끝났는지를 표시하는 boolean값이다.
    # 이 값이 false이면 공격을 했으나 반격을 하지 않은 것이고,
    # 이 값이 True이면 공격과 반격이 이루어져 결과가 난 것이다.
    is_end = models.BooleanField(default=False)

    # 중요한 것은 updated_at 값이다. 이 값을 기준으로 game_list에서 Game들이 정렬된다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def is_host(self, user):
    #     return self.host == user

    def __str__(self):
        return f"{self.host.username} vs {self.guest.username}"

    # 편의성을 위해 한 Game의 url을 구하는 함수를 만들었다.
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
