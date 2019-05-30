from django.urls import path 

from . import views

urlpatterns = [
    path('', views.search, name="search"),
    path('upload/', views.upload, name="upload"),
]
