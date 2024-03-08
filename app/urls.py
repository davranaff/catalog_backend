from django.urls import path
from app import views

urlpatterns = [
    path('menu/', views.MenuViewSet.as_view({'get': 'list', 'post': 'create'}), name='menu_list'),
    path('menu/<pk>/', views.MenuViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='menu_list'),
]
