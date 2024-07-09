
from django.contrib import admin
from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path('',views.home,name="home"),
    path('books/',views.list_books,name="list_books"),
    path('book_api/',views.get_post_book_api,name="get_post"),
    
]
