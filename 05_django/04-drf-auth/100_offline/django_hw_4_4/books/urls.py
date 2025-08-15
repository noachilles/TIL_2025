from django.urls import path
from . import views

urlpatterns = [
    # 1번 기능 - 회원이 아니어도 리스트 조회 가능
    path('', views.book_list),
    # 2번 기능 - 회원에게만 도서 대출 기능 제공
    path('borrow/<book_isbn>/', views.borrow_book),
]
