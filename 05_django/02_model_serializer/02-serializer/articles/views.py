from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializer import ArticleListSerializer, ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST']) # 이게 없으면 화면이 표시되지 않음 - django 기본 기능이 아닌 이상
def article_get_or_create(request):
    if request.method == 'GET':
        # 전체 게시글 조회
        # models로부터 article 클래스를 받아와야 함 (models에서 먼저 DB를 만들고, urls 연동하고, views에서 함수 정의)
        articles = Article.objects.all()
        # id, title만 보여주고 싶음 -> serializer를 정의
        # 보통 클래스에 하나의 객체를 넣지만, many 속성으로 여러 개 입력 가능
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화 마친 객체의 data만 사용자에게 반환
        return Response(serializer.data)    # status에 대한 정보도 넘길 수 있음
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # 사용자가 보낸 data로 article 생성
        # 그 정보가 유효한지 검증
        if serializer.is_valid():
            serializer.save()
            # 정상: 저장
            # 반환
            return Response(serializer.data)