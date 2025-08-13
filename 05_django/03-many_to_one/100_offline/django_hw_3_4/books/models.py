from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre_of_book = models.ForeignKey('books.Genre', 
                                      related_name="genre_of_book", 
                                      on_delete=models.CASCADE,
                                      default='')

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name