from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response

from genres.models import GenresModel
from. serializers import BookSerializers, PageSerializers
from .models import BookModel, PageModel, ReadingSession
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .decorators import check_payment_status
from django.db.models import Q

# Create your views here.
def home_page(request):
    sort = request.GET.get("sort")
    books = BookModel.objects.all()
    if sort:
        books = BookModel.objects.filter(genres__genres = sort)
        
    context = {
        'books':books
    }
    return render(request,"home/home.html",context)

def list_books_page(request):
    keyword = request.GET.get("keyword")

    sort = request.GET.get("sort")
    books = BookModel.objects.all()
    if sort:
        books = BookModel.objects.filter(genres__genres=sort)  # Đúng

    if keyword:
        books = BookModel.objects.filter(
            Q(bookname__icontains = keyword)
            | Q(author__icontains = keyword)
            
        ) 
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
@check_payment_status
def reading_page(request, book_id):
    print("Reading page")
    if not request.user.is_authenticated:
        return render(request, 'home/not_logged_in.html')
    book = BookModel.objects.get(id=book_id)
    pages = PageModel.objects.filter(book=book)
    user = request.user
    refresh = RefreshToken.for_user(user)
    last_bookmarked_page = ReadingSession.objects.filter(user=user, page__book=book).order_by('-created_at').first()
    # Nếu có trang đánh dấu, lấy ID của trang đó
    bookmarked_page_id = last_bookmarked_page.page.id if last_bookmarked_page else None

    context = {
        'book': book,
        'pages': pages,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'bookmarked_page_id': bookmarked_page_id  # Truyền ID trang đã đánh dấu lớn nhất vào context
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


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import smtplib
from email.mime.text import MIMEText
from .utils import sending_email
@csrf_exempt  # Tắt CSRF để test nhanh (không nên dùng trong sản phẩm thật)
def signup_newsletter(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            first_name = data.get("first_name")
            last_name = data.get("last_name")

            if not email:
                return JsonResponse({"error": "Email là bắt buộc"}, status=400)

            email_body = f"Chào {first_name} {last_name},\n\nCảm ơn bạn đã đăng ký nhận bản tin!"
            sending_email(email_body, email)

            return JsonResponse({"message": "Đăng ký thành công!"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Chỉ hỗ trợ POST"}, status=405)