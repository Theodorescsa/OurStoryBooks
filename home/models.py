from django.db import models
from genres.models import GenresModel
from django.contrib.auth.models import User

# Create your models here.
class BookModel(models.Model):
    user = models.ManyToManyField(User)
    genres = models.ManyToManyField(GenresModel)
    bookname = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='images/', null=True)
    author = models.TextField(null=True)
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

class PurchasedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchased_books')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='purchased_by_users')
    purchase_date = models.DateTimeField(auto_now_add=True)
    price_at_purchase = models.FloatField(blank=True,null=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'book')  # Đảm bảo mỗi người dùng chỉ mua một cuốn sách một lần
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.user.username} purchased {self.book.bookname} on {self.purchase_date.strftime('%Y-%m-%d')}"
    
    def update_status(self):
        self.is_paid = True
        self.save()
        return self.is_paid

class ReadingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_sessions')
    page = models.ForeignKey(PageModel, on_delete=models.CASCADE, related_name='reading_sessions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the ReadingSession object.

        The string representation of the object will be in the format:
        "user.username reading page.page_number on page.created_at"

        :return: A string representation of the ReadingSession object
        :rtype: str
        """
        return f"{self.user.username} reading page {self.page.page_number} on {self.page.created_at}"  # noqa: E501 self.
    