from django.contrib.auth.models import AbstractUser

# 기본 유저 모델을 대체하도록 - settings.py를 수정한다.
class User(AbstractUser):
    pass