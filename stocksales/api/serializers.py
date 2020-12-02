from rest_framework import serializers
# from rest_framework import serializers.TokenSerializer
from stocksales.models import *
# from rest_auth.serializers import TokenSerializer
from django.contrib.auth import get_user_model


class PhoneTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneType
        fields = ['type_name']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['brand_name', 'phone_type']


class PhoneModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneModel
        fields = ['user', 'phone_type',
                  'brand', 'model_name', 'processor', 'ram', 'camera_front', 'camera_back', 'screen_size',
                  'screen_resolution', 'battery_life', 'battery_type', 'operating_system']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name']


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = ['storage_size']


class ProductStockInSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductStockIn
        fields = ['user', 'phone_type', 'brand', 'phone_model', 'color',
                  'storage', 'buying_price', 'selling_price', 'timestamp_in']


class StockToShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockToShop
        fields = ['product', 'shop_to']


class ShopToShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopToShop
        fields = ['product_stock_in', 'shop_from', 'shop_to']


class ShopProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopProduct
        fields = ['product_stock_in', 'shop_available', 'status']


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ['product_stock_in', 'shop', 'discount', 'markup', 'actual_selling_price']
