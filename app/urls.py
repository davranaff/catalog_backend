from django.urls import path
from app import views


urlpatterns = [
    path('menu/', views.MenuAPI.as_view(), name='menu'),
]
