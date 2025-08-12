from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article

def model_to_dict(article):
    '''
    Article 객체를 딕셔너리로 변환하는 함수
    :param article: Article 객체
    :return: Article 객체를 딕셔너리로 변환한 결과
    '''
    return {
        'id': article.id,
        'title': article.title,
        'content': article.content
    }


@api_view(['POST'])
def article_create(request):
    # 데이터 객체를 만드는(생성하는) 첫번째 방법
    article = Article() 
    
    article.title = request.data.get('title') 
    article.content = request.data.get('content')
    
    # 데이터 객체를 만드는(생성하는) 두번째 방법
    # article = Article(title=request.data.get('title'), content=request.data.get('content'))
    
    article.save() # 데이터베이스에 저장
    
    # 데이터베이스에 저장하는 세번째 방법  -> 위 두 방법과 달리 객체 생성과 동시에 데이터베이스에 저장됨
    # Article.objects.create(title=request.data.get('title'), content=request.data.get('content'))
    
    # 반환값으로 article.id와 status.HTTP_201_CREATED를 응답 코드로 반환
    return JsonResponse({'id': article.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()  # 저장된 모든 article 데이터를 가져옴
    # title이 'article_02'인 데이터만 가져옴 존재하지 않으면 빈 리스트 반환
    # articles = Article.objects.filter(title='title1')
    
    # QeurySet 객체를 순회하며 각각의 데이터를 딕셔너리로 변환
    if articles:  # articles가 존재하면
        data = [model_to_dict(article) for article in articles]
        return JsonResponse({'data': data})  # articles가 존재하면 데이터를 반환
    return JsonResponse({'data': []})  # articles가 존재하지 않으면 빈 리스트 반환
    # return JsonResponse(data, safe=False)  # 딕셔너리가 아닌 데이터를 반환할 때 safe=False로 설정

@api_view(['GET'])
def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    # article = Article.objects.get(title='title')  # title 필드에 저장된 값이 'title'인 데이터를 가져옴
    return JsonResponse(model_to_dict(article))

@api_view(['PUT'])
def article_update(request, pk):
    article = Article.objects.get(pk=pk) # 수정할 article 데이터를 가져옴
    # 수정할 데이터를 request.data로부터 가져와서 수정
    article.title = request.data.get('title') 
    article.content = request.data.get('content') 
    article.save() # 수정된 데이터를 저장
    return JsonResponse(model_to_dict(article))


@api_view(['DELETE'])
def article_delete(request, pk):
    article = Article.objects.get(pk=pk)  # 삭제할 article 데이터를 가져옴
    article.delete() # 데이터 삭제
    return JsonResponse({'message': ' 삭제 완료~'})
