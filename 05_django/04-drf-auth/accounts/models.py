from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 인증과 관련된 테이블을 설정할 때,
    # 장고가 기본으로 제공해주는 필드들을
    # 수정 없이 그대로 사용한다고 하더라도
    # 장고는 User 모델을 custom해서 등록하기를 '강력히 권장'
    
    # django에게, 이 class가 기존 auth class를 대체할 것임을 설정  
    pass
