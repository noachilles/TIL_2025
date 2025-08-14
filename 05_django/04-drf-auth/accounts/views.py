from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm  # 장고 내장 로그인 폼
from django.contrib.auth import login as auth_login  # 장고 내장 로그인 함수

# Session Authentication test function
@api_view(["POST"])
def login(request):
    form = AuthenticationForm(request, request.POST)  # 사용자가 입력한 데이터를 폼에 넣음
    if form.is_valid():  # 유효성 검사
        user = form.get_user()  # form에서 user 객체를 가져옴
        auth_login(request, user)  # 로그인 함수 실행
        session_id = request.session.session_key  # 세션 키를 가져옴
        response_data = {
            'message': 'Login successful',
            'session_id': session_id
        }
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

