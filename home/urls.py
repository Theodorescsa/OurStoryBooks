
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .viewsets import BookModelViewSet, PageModelViewSet, PurchasedBookViewSet, ReadingSessionViewSet

router = DefaultRouter()
router.register(r'books', BookModelViewSet)
router.register(r'pages', PageModelViewSet)
router.register(r'purchased_books', PurchasedBookViewSet)
router.register(r'reading-sessions', ReadingSessionViewSet, basename='reading-session')

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
    path('reading-book/<int:book_id>/',views.reading_page,name="reading_page"),
    path('home-api/', include(router.urls)),
]
