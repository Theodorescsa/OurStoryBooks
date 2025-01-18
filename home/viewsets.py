# views.py
from rest_framework import viewsets
from .models import BookModel, PageModel
from .serializers import BookSerializers, PageSerializers

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

class PageModelViewSet(viewsets.ModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializers