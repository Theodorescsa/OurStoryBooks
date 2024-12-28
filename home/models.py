from django.db import models
from genres.models import GenresModel
from django.contrib.auth.models import User

# Create your models here.
class BookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    genres = models.ManyToManyField(GenresModel)
    bookname = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='images/', null=True)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.FloatField(null=True)
    description = models.TextField()
    published = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.bookname


class PageModel(models.Model):
    book = models.ForeignKey(
        BookModel, 
        on_delete=models.CASCADE, 
        related_name="book_pages" 
    )
    chapter = models.CharField(max_length=200,blank=True)
    page_number = models.PositiveIntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('book', 'page_number') 
        ordering = ['page_number'] 

    def __str__(self):
        return f"{self.book.bookname} - Page {self.page_number}"
