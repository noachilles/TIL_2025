from django.urls import path
from . import views

urlpatterns = [
    # N번 작가의 상세 정보
        # 사용자가 pk에 대한 정보 담아서 보냄
    path('<int:author_pk>/', views.author_detail),
    path('', views.author_list),
]
