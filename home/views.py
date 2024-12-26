from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from. serializers import BookSerializers
from .models import BookModel
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.
def home_page(request):
    # user = User.objects.get(username = request.user.username)
    books = BookModel.objects.all()
    context = {
        'books':books
    }
    return render(request,"home/home.html",context)

def list_books_page(request):
    books = BookModel.objects.all()
    context = {
        'books':books
    }
    return render(request,"home/books.html",context)

def book_detail_page(request,id):
    book = BookModel.objects.get(id=id)
    context = {
        'book':book
    }
    return render(request,"home/bookdetail.html",context)

def videos_and_photos_page(request):
    return render(request,'home/videos_and_photos.html')

def photos_page(request):
    return render(request,'home/photos.html')

def find_adam_page(request):
    return render(request,'home/findadam.html')

def resources_page(request):
    return render(request,'home/resources.html')

def news_announ_page(request):
    return render(request,'home/news_announcement.html')

def about_page(request):
    return render(request,'home/about.html')

def write_adam_page(request):
    return render(request,'home/writeadam.html')
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