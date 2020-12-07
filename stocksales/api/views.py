from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from stocksales.api.serializers import *
from django.core import serializers
import json
from rest_framework.renderers import JSONRenderer

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User
from stocksales.models import *


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def reg_phone_type(request):
    if request.method == 'POST':
        serializer = PhoneTypeSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            phone_type_s = serializer.save()

            shop_id = phone_type_s.id
            shop_obj = PhoneType.objects.all()
            # data['Response'] = 'Position registered successfully'
            shop_type = serializers.serialize(
                "json", shop_obj)
            data['shop_type_model'] = shop_type

        else:
            data = serializer.errors
        return Response(data)


# Register Brand
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def reg_brand(request):
    if request.method == 'POST':
        # First getting the object id
        serializer = BrandSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            # validatedData = serializer.validated_data
            serializer.save()
            all_brands = Brand.objects.all()

            brands_obj = serializers.serialize(
                "json", all_brands)
            data['brands'] = brands_obj

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def reg_phone_model(request):
    if request.method == 'POST':
        serializer = PhoneModelSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            phone_model_s = serializer.save()
            phone_model_obj = PhoneModel.objects.all()
            # data['Response'] = 'Position registered successfully'
            phone_model_s = serializers.serialize(
                "json", phone_model_obj)
            data['shop_type_model'] = phone_model_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def reg_color(request):
    if request.method == 'POST':
        serializer = ColorSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            color_obj = Color.objects.all()
            # data['Response'] = 'Position registered successfully'
            color_s = serializers.serialize(
                "json", color_obj)
            data['color_objects'] = color_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def reg_storage(request):
    if request.method == 'POST':
        serializer = StorageSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            storage_obj = Storage.objects.all()
            # data['Response'] = 'Position registered successfully'
            storage_s = serializers.serialize(
                "json", storage_obj)
            data['storage_details'] = storage_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def product_stock_in(request):
    if request.method == 'POST':
        serializer = ProductStockInSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            product_stock_in_obj = ProductStockIn.objects.all()
            # data['Response'] = 'Position registered successfully'
            product_stock_in_s = serializers.serialize(
                "json", product_stock_in_obj)
            data['product_stock_in'] = product_stock_in_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def stock_to_shop(request):
    if request.method == 'POST':
        serializer = StockToShopSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            stock_to_shop_obj = StockToShop.objects.all()
            # data['Response'] = 'Position registered successfully'
            stock_to_shop_s = serializers.serialize(
                "json", stock_to_shop_obj)
            data['stock_to_shop_objects'] = stock_to_shop_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_to_shop(request):
    if request.method == 'POST':
        serializer = ShopToShopSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            shop_to_shop_obj = ShopToShop.objects.all()
            # data['Response'] = 'Position registered successfully'
            shop_to_shop_s = serializers.serialize(
                "json", shop_to_shop_obj)
            data['shop_to_shop_objects'] = shop_to_shop_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_product(request):
    if request.method == 'POST':
        serializer = ShopProductSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            shop_product_obj = ShopProduct.objects.all()
            # data['Response'] = 'Position registered successfully'
            shop_product_s = serializers.serialize(
                "json", shop_product_obj)
            data['shop_product_objects'] = shop_product_s

        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def sales_product(request):
    if request.method == 'POST':
        serializer = SalesSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            sales_obj = Sales.objects.all()
            # data['Response'] = 'Position registered successfully'
            sales_s = serializers.serialize(
                "json", sales_obj)
            data['shop_product_objects'] = sales_s

        else:
            data = serializer.errors
        return Response(data)


# Stock admin
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def stock_admin(request):
    if request.method == 'GET':

        data = {}

        phone_type_objs = PhoneType.objects.all()
        brand_objs = Brand.objects.all()
        phone_model_objs = PhoneModel.objects.all()
        color_objs = Color.objects.all()
        storage_objs = Storage.objects.all()

        # data['Response'] = 'Position registered successfully'
        phone_type_s = serializers.serialize(
            "json", phone_type_objs)
        brand_s = serializers.serialize(
            "json", brand_objs)
        phone_model_s = serializers.serialize(
            "json", phone_model_objs)
        phone_model_str = json.loads(phone_model_s)
        if phone_model_str:
            j = 0
            for phone_model_ss in phone_model_str:

                user_id = phone_model_ss['fields']['user']
                phone_type_id = phone_model_ss['fields']['phone_type']
                brand_id = phone_model_ss['fields']['brand']

                user_str = serializers.serialize(
                    "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

                user_json = json.loads(user_str)
                print('======')
                print(user_json[0])
                if user_json:
                    phone_model_str[j]['fields']['user'] = user_json[0]

                phone_type_str = serializers.serialize(
                    "json", PhoneType.objects.filter(id=phone_type_id))
                phone_type_json = json.loads(phone_type_str)
                if phone_type_json:
                    phone_model_str[j]['fields']['phone_type'] = phone_type_json[0]

                brand_str = serializers.serialize(
                    "json", Brand.objects.filter(id=brand_id))
                brand_json = json.loads(brand_str)
                if brand_json:
                    phone_model_str[j]['fields']['brand'] = brand_json[0]

                j = j+1
        color_s = serializers.serialize(
            "json", color_objs)
        storage_s = serializers.serialize(
            "json", storage_objs)
        data['phone_type_objects'] = phone_type_s
        data['brand_objects'] = brand_s
        data['phone_model_objects'] = phone_model_str
        data['color_objects'] = color_s
        data['storage_objects'] = storage_s
        return Response(data)
