from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    # 이미 pjt url에서 articles라고 정의함  
    # 따라서 articles라고 표기할 필요가 없음
    path('<int:article_pk>', views.detail)
]