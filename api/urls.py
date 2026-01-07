from django.urls import path
from api.views import *
from . import views



urlpatterns = [
    path('posts/', views.product_list_create_api_view, name='post-list-create'),
    path('posts/<int:pk>/', views.product_update_api_views, name='post-detail'),
    path('categories/', views.category_list_create_api_view, name='category-list-create'),
    path('categories/<int:pk>/', views.category_detail_api_view, name='category-detail'),
    path('categories/<int:pk>/update/', views.category_update_api_views, name='category-update'),
    path('categories/<int:pk>/delete/', views.category_delete_api_view, name='category-delete'),
    
]
    
    
