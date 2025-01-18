from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import GenresModel
from .serializers import GenresSerializer
# Create your views here.
class GenresModelViewSet(viewsets.ModelViewSet):
    queryset = GenresModel.objects.all()
    serializer_class = GenresSerializer
    