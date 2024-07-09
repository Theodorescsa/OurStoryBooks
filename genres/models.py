from django.db import models
# from home.models import BookModel
# Create your models here.
class GenresModel(models.Model):
    genres = models.CharField(max_length=100)
    description = models.TextField()
    # book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.genres