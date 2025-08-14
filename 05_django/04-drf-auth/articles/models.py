from django.db import models
from django.conf import settings


# articles/models.py
class Article(models.Model):
    
    # django가 기본적으로 User에 대한 Auth 모델을 지원
    # User 모델이란 내용은, 매우 복잡한 관계를 갖고 있음
    # 우리는 현재 '활성화'된 유저 모델에 대한 정보를
    # 장고 개발자들끼리는 AUTH_USER_MODEL에 적기로 약속
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
