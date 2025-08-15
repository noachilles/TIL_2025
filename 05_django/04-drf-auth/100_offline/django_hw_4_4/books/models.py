from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name='books')
    published_date = models.DateField()
    borrowed = models.BooleanField(default=False)
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title