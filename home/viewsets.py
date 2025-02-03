# views.py
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from .models import BookModel, PageModel, PurchasedBook
from .serializers import BookSerializers, PageSerializers, PurchasedBookSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

class PageModelViewSet(viewsets.ModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializers
    
class PurchasedBookViewSet(viewsets.ModelViewSet):
    queryset = PurchasedBook.objects.all()  # Lấy tất cả các bản ghi PurchasedBook
    serializer_class = PurchasedBookSerializer
    permission_classes = [IsAuthenticated]  # Chỉ cho phép người dùng đã đăng nhập

    def get_queryset(self):
        # Lọc các sách đã mua của người dùng hiện tại
        return PurchasedBook.objects.filter(user=self.request.user)