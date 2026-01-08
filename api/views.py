from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics , response, status,permissions
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_api_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message':'Login successful!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
        
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_api_view(request):
    try:
        logout(request)
        return Response({'message':'Logout successful!'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message':'An error occurred during logout.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET','POST'])
@permission_classes([permissions.AllowAny])
def product_list_create_api_view(request):
    if request.method == 'GET':
        serializers = ProductSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        print(serializers.data)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['PATCH','PUT'])
@permission_classes([permissions.AllowAny]) 
def product_update_api_views(request,pk):
    product = Product.objects.filter(id=pk).first()
    if not product:
        return Response({'message':'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializers = ProductSerializer(product, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializers = ProductSerializer(product, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def product_delete_api_view(request,pk):
    product = Product.objects.filter(id=pk).first()
    if not product:
        return Response({'message':'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({'message':'Product deleted successfully!'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def product_detail_api_view(request,pk):    
    product = Product.objects.filter(id=pk).first()
    if not product:
        return Response({'message':'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = ProductSerializer(product)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['POST','GET'])
def category_list_create_api_view(request):
    if request.method == 'POST':
        serializers = CategorySerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        print(serializers.data)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['PUT','PATCH'])
def category_update_api_views(request,pk):
    category = Category.objects.filter(id=pk).first()
    if not category:
        return Response({'message':'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializers = CategorySerializer(category, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializers = CategorySerializer(category, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def category_delete_api_view(request,pk):
    category = Category.objects.filter(id=pk).first()
    if not category:
        return Response({'message':'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        category.delete()
        return Response({'message':'Category deleted successfully!'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def category_detail_api_view(request,pk):    
    category = Category.objects.filter(id=pk).first()
    if not category:
        return Response({'message':'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = CategorySerializer(category)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['POST','GET'])
def post_list_create_api_view(request):
    if request.method == 'POST':
        serializers = PostSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        print(serializers.data)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

@api_view(['PUT','PATCH'])
def post_update_api_views(request,pk):
    post = Post.objects.filter(id=pk).first()
    if not post:
        return Response({'message':'Post not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializers = PostSerializer(post, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializers = PostSerializer(post, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)