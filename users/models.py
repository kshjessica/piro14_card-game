from django.db import models
from django.contrib.auth.models import AbstractUser
from itertools import chain


class User(AbstractUser):
    win = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)

    def participated_games(self):
        """
        최근 업데이트 순으로 정렬된
        user가 참가한 모든 게임의 list를 반환함
        """
        hosted_games = self.hosted_games.all()
        guested_games = self.guested_games.all()
        participated_games = chain(hosted_games, guested_games)
        participated_games = sorted(participated_games, key=lambda x: x.updated_at)[
            ::-1
        ]
        return participated_games