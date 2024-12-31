from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from. serializers import BookSerializers, PageSerializers
from .models import BookModel, PageModel
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def home_page(request):
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
    if not request.user.is_authenticated:
        return render(request, 'home/not_logged_in.html')
    book = BookModel.objects.get(id=id)
    user = request.user
    refresh = RefreshToken.for_user(user)
    context = {
        'book':book,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        
    }
    return render(request,"home/bookdetail.html",context)

@login_required
def reading_page(request, book_id):
    if not request.user.is_authenticated:
        return render(request, 'home/not_logged_in.html')
    book = BookModel.objects.get(id=book_id)
    pages = PageModel.objects.filter(book=book)
    context = {
        'book': book,
        'pages': pages
    }
    return render(request,'home/reading_page.html',context)

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

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])  # Yêu cầu xác thực JWT
def get_post_api(request):
    if request.method == "GET":
        model_type = request.query_params.get("model", "BookModel")  # Lấy loại model từ query param
        if model_type == "PageModel":
            model = PageModel.objects.all()
            serializers = PageSerializers(model, many=True)
        else:  # Mặc định lấy BookModel
            model = BookModel.objects.all()
            serializers = BookSerializers(model, many=True)
        return Response(serializers.data)

    elif request.method == "POST":
        model_type = request.data.get("model", "BookModel")  # Kiểm tra loại model từ dữ liệu POST
        if model_type == "PageModel":
            serializer = PageSerializers(data=request.data)
        else:  # Mặc định sử dụng BookSerializers
            serializer = BookSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return redirect("home:list_books")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])  # Yêu cầu xác thực JWT
def get_put_delete_api(request, id):
    model_type = request.query_params.get("model", "BookModel")  # Xác định loại model từ query param
    if model_type == "PageModel":
        model = get_object_or_404(PageModel, id=id)
        serializer_class = PageSerializers
    else:  # Mặc định lấy BookModel
        model = get_object_or_404(BookModel, id=id)
        serializer_class = BookSerializers

    if request.method == "GET":
        serializer = serializer_class(model)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = serializer_class(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
