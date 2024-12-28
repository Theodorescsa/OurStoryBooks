from rest_framework import serializers
from .models import BookModel, PageModel
class BookSerializers(serializers.ModelSerializer):
    class Meta():
        model = BookModel
        fields = '__all__'
        
class PageSerializers(serializers.ModelSerializer):
    class Meta():
        model = PageModel
        fields = '__all__'