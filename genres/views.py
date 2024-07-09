from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import GenresModel
from .serializers import GenresSerializer
# Create your views here.
def list_genres(request):
    return render(request,"")

@api_view(["GET","POST"])
def get_post_genres_api(request):
    if request.method == "GET":
        model = GenresModel.objects.all()
        serializers = GenresSerializer(model,many = True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = GenresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("genres:list_genres")


@api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])
def get_put_delete_api(request, id):
    model = get_object_or_404(GenresModel, id=id)

    if request.method == "GET":
        serializer = GenresSerializer(model)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GenresSerializer(model, data=request.data)
        print("geellsadlasd")
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return redirect('genres:detail',id)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
