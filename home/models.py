from django.db import models
from genres.models import GenresModel
# Create your models here.
class BookModel(models.Model):
    genres = models.ManyToManyField(GenresModel)
    bookname = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='images/',null=True)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.FloatField(null=True)
    description = models.TextField()
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.bookname