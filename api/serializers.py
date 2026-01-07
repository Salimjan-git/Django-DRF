from rest_framework import serializers
from .models import Post, Category, Product

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock')
        
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['price'] = 100
        repr['count'] = 12
        return repr