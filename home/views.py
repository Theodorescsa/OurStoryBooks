from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from. serializers import BookSerializers
from .models import BookModel
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    return render(request,"home/home.html")
def list_books(request):
    return render(request,"home/books.html")
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])  # Yêu cầu xác thực JWT
def get_post_book_api(request):
    if request.method == "GET":
        model = BookModel.objects.all()
        serializers = BookSerializers(model,many = True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("home:list_books")

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def get_put_delete_api(request, id):
    model = get_object_or_404(BookModel, id=id)

    if request.method == "GET":
        serializer = BookSerializers(model)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BookSerializers(model, data=request.data)
        print("geellsadlasd")
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return redirect('home:detail',id)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)