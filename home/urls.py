
from django.contrib import admin
from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
    path('',views.home_page,name="home"),
    path('books/',views.list_books_page,name="list_books"),
    path('books/<int:id>/',views.book_detail_page,name="book_detail"),
    path('videos&photos/',views.videos_and_photos_page,name="videos_and_photos"),
    path('photos/',views.photos_page,name="photos"),
    path('find-adam/',views.find_adam_page,name="find_adam"),
    path('resources/',views.resources_page,name="resources"),
    path('news_announ/',views.news_announ_page,name="news_announ"),
    path('about_us/',views.about_page,name="about_us"),
    path('write_adam/',views.write_adam_page,name="write_adam"),
    path('book_api/',views.get_post_book_api,name="get_post"),
    
]
