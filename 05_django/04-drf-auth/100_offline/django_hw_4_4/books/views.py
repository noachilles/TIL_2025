from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer
from django.shortcuts import get_object_or_404
# permission 제한을 위한 import
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def borrow_book(request, book_isbn):
    # isbn값이 같은 자료를 받아옴
    book = get_object_or_404(Book, isbn=book_isbn)
    # 현재 빌릴 수 있는 경우라면
    if book.borrowed == False:
        # 빌린다(borrowed 값을 True로 저장)
        book.borrowed = True
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data)
    else:
        return Response({"detail": "this book is borrowed. Please try again on next time."})
        