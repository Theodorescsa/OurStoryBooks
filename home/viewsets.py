# views.py
from rest_framework import viewsets
from .models import BookModel
from .serializers import BookSerializers

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
