from django.db import models
from django.contrib.auth.models import AbstractUser
from itertools import chain


class User(AbstractUser):
    # Django의 기본 유저 모델을 상속받아 사용한다.
    # 거기에 Win과 Lose만 추가했다.
    # Game에서 공격과 반격이 오간 후 결과가 나왔을 때,
    # 즉 games 앱의 game_counter 뷰 에서 결과를 산출할 때
    # 각각 Game의 host와 guest의 win과 lose를 계산해준다.
    win = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)

    def participated_games(self):
        """
        최근 업데이트 순으로 정렬된
        user가 참가한 모든 게임의 list를 반환한다.
        이 함수는 games 앱의 game_list 뷰에서
        유저가 참가한 모든 게임의 리스트를 보여줄 때 사용된다.
        """
        hosted_games = self.hosted_games.all()
        guested_games = self.guested_games.all()
        participated_games = chain(hosted_games, guested_games)
        participated_games = sorted(participated_games, key=lambda x: x.updated_at)[
            ::-1
        ]
        return participated_games