from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AuthorSerializer, AuthorListSerializer
from .models import Author
from django.db.models import Count

# Create your views here.
@api_view(['GET'])
def author_detail(request, author_pk):
    # 저자 한 명에 대한 상세 정보 반환
        # 직렬화 필요
    author = Author.objects.get(pk=author_pk)
    author = Author.objects.annotate(book_count=Count('book')).get(pk=author_pk)
    print(author.book_count)
    # 기본적인 출력
    # print(author.pk, author.name, author.book_set.all())

    serializers = AuthorSerializer(author)
    return Response(serializers.data)

@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all()
    serializers = AuthorListSerializer(authors, many=True)
    return Response(serializers.data)