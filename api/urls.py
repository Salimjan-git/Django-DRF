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
    path('products/', views.product_list_create_api_view, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail_api_view, name='product-detail'),
    path('products/<int:pk>/update/', views.product_update_api_views, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete_api_view, name='product-delete'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', views.login_api_view, name='login'),
    path('logout/', views.logout_api_view, name='logout'),
    
    
    
]
    
    
