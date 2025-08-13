from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    # 장고가 갖고 있는 집계 함수
    article = Article.objects.annotate(num_of_comments=Count('comment')).get(
        pk=article_pk
    )

    # article 객체가 num_of_comments를 갖고 serializer로 전달됨
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 하나 지정해 그곳에 댓글 생성
    article = Article.objects.get(pk=article_pk)
    # 댓글 생성은 사용자가 보낸 content 정보 저장
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        # DB 반영
        serializer.save(article=article)
        # 완성된 댓글 정보를 사용자에게 반환
        return Response(serializer.data)
    pass


# 모든 댓글 조회
@api_view(['GET'])
def comment_list(request):
   pass

# 댓글 pk 값으로 조회, 삭제, 수정
@api_view(['GET'])
def comment_detail(request, comment_pk):
    pass
   

