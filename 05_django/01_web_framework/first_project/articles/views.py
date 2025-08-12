from django.shortcuts import render
# django가 갖고 있는 http에 따른 응답 방식
from django.http import JsonResponse
# RESTful API를 만들도록 해주는 framework
from rest_framework.decorators import api_view

# Create your views here.
# 행위 -> RESTful API를 위한 것
# GET 요청일 때만 아래 함수가 동작하도록 하고 싶고, 그렇게 함수 꾸미기
@api_view(['GET', 'POST'])
def index(request):
    # 모든 view 함수는 첫번째 인자 request 고정
        # 물론 인자명 request는 다른 이름이어도 상관은 없지만
        # django의 가이드 상, request이므로 다른 이름으로 적지 않음
    # 응답: Json 형태로 Response -> {'message':'Hello, Django!'}
    # request에는 사용자의 모든 요청과 관련 정보가
    if request.method == 'POST':
        return JsonResponse({'message':'Hello, Django!'})
    elif request.method == 'GET':
        return JsonResponse({'message':'Hello, Django!'})
    
def detail(request, article_pk):
    # 원래 여기서 model 거쳐서 실제 1번 게시글 가져와야~,,
    data = {
        'id': article_pk,
        'message': f'Information about {article_pk}.'
    }
    return JsonResponse(data)