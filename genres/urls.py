
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'genres', views.GenresModelViewSet)
app_name = "genres"
urlpatterns = [
    path('',include(router.urls)),
    # path('',views.list_genres,name="list_genres"),
    
]
