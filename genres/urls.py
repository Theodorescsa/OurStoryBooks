
from django.contrib import admin
from django.urls import path
from . import views
app_name = "genres"
urlpatterns = [
    # path('',views.list_genres,name="list_genres"),
    path('genres_api',views.get_post_genres_api,name="get_post"),
    
]
