from django.contrib import admin
from django.urls import path, include
from . import views

app_name='base_asset'
urlpatterns = [
    path('bf/', views.DocumentCreateView.as_view(), name='baseform'),
]