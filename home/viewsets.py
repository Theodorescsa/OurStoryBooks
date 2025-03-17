# views.py
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import BookModel, PageModel, PurchasedBook, ReadingSession
from .serializers import BookSerializers, PageSerializers, PurchasedBookSerializer, ReadingSessionSerializer

from django.contrib.auth.models import User
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


class ReadingSessionViewSet(viewsets.ModelViewSet):
    queryset = ReadingSession.objects.all()
    serializer_class = ReadingSessionSerializer
    permission_classes = [IsAuthenticated]  # Chỉ cho phép người dùng đã đăng nhập

    def perform_create(self, serializer):
        """Đặt user là người dùng hiện tại khi tạo phiên đọc"""
        serializer.save(user=self.request.user)
    @action(detail=False, methods=['post'])
    def bookmark(self, request):
        page_id = request.data.get('page')
        user_id = request.data.get('user_id')

        if not page_id:
            return Response({"error": "Dữ liệu không hợp lệ!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Kiểm tra xem người dùng đã đánh dấu trang chưa
            existing_session = ReadingSession.objects.filter(user=request.user, page__id=page_id).first()
            
            if existing_session:
                return Response({"error": "Bạn đã đánh dấu trang này rồi!"}, status=status.HTTP_400_BAD_REQUEST)

            # Tạo mới ReadingSession
            user = User.objects.get(id=user_id)
            page = PageModel.objects.get(id=page_id)
            session = ReadingSession.objects.create(user=user, page=page)
            return Response({"success": True, "message": "Đã đánh dấu trang thành công!"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)