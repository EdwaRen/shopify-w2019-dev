from .models import *
from rest_framework import serializers

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "name", "shop", 'getValue', 'manifest')

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = '__all__'