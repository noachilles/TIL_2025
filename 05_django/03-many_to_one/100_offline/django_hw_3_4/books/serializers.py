
from rest_framework import serializers
from .models import Book, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class GenreSerializer(serializers.ModelSerializer):
    
    class BookdTitleAuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('title', 'author',)
    genre_of_books = BookdTitleAuthorSerializer(source='genre_of_book', many=True, read_only=True)
    num_of_books = serializers.SerializerMethodField()
    
    def get_num_of_books(self, obj):
        return obj.num_of_books
    class Meta:
        model = Genre
        fields = ('name', 'num_of_books', 'genre_of_books',)