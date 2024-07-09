from .models import GenresModel
from rest_framework import serializers

class GenresSerializer(serializers.ModelSerializer):
    class Meta():
        model = GenresModel
        fields = '__all__'