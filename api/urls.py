from django.urls import path
from api.views import *

urlpatterns = [
    path('posts/', PostListAPIViews.as_view(),name='post-list-create'),
    path('posts/<int:pk>/',PostDatailAPIViews.as_view(), name='post-detail'),
]