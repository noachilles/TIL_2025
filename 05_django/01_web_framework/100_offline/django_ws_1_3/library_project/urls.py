'''
- 새로운 가상 환경을 생성하고, 가상 환경을 활성화한다.
- 활성화된 가상환경에서 django 어플리케이션에 필요한 의존성을 설치한다.
- 도서 리스트 반환 View 함수를 작성한다.
- 도서 리스트는 한번에 5개의 목록을 JSON 형식으로 반환한다.
- URL 설정을 통해 'http://127.0.0.1:8000/books/' 경로로 요청을 처리한다.
- 쿼리 파라미터 'page'를 통해 페이지 번호를 받는다.
- 단, page 파라미터가 없을 경우에도 첫번째 페이지로 간주하여 결과값을 반환한다.
- 요청 받은 페이지 수가 전체 도서 정보 수를 넘어서면, 별도 예외 처리 없이 빈 리스트가 반환되어도 무관하다.
'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include('books.urls'))
]
