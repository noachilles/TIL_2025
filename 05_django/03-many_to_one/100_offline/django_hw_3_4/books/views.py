from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre
from .serializers import GenreSerializer
from django.db.models import Count

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = Genre.objects.get(pk=genre_pk)
    genre = Genre.objects.annotate(num_of_books=Count('genre_of_book')).get(pk=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)
    