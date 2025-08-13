from django.db import models
# from authors.models import Author

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

