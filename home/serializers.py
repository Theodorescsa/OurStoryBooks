from rest_framework import serializers
from .models import BookModel, PageModel, PurchasedBook
class BookSerializers(serializers.ModelSerializer):
    class Meta():
        model = BookModel
        fields = '__all__'
        
class PageSerializers(serializers.ModelSerializer):
    class Meta():
        model = PageModel
        fields = '__all__'
        


class PurchasedBookSerializer(serializers.ModelSerializer):
    book_detail = BookSerializers(source='book', read_only=True)
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = PurchasedBook
        fields = ['id', 'user', 'user_name', 'book', 'book_detail', 'purchase_date', 'price_at_purchase', 'is_paid']

from rest_framework import serializers
from .models import ReadingSession

class ReadingSessionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Hiển thị username thay vì ID
    page = serializers.StringRelatedField()  # Hiển thị thông tin trang thay vì ID

    class Meta:
        model = ReadingSession
        fields = ['id', 'user', 'page', 'created_at']
