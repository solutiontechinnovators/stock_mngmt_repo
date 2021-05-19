from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from stocksales.api.serializers import *
from django.core import serializers
import json
from django.db.models import Count
from rest_framework.renderers import JSONRenderer

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User
from stocksales.models import *
from datetime import datetime, date


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
        posted_data = request.data
        imei_lists = posted_data['imei_no']
        
        for imei in imei_lists:
            posted_data['imei_no'] = imei
            serializer = ProductStockInSerializer(data=posted_data)
            data = {}
            
            if serializer.is_valid():
                user = request.user
                location = Shop.objects.filter(shop_no=100)
                serializer.save(user=user, stock_loc=location[0])
                product_stock_in_obj = 'data saved'
                # data['Response'] = 'Position registered successfully'
                # product_stock_in_s = serializers.serialize(
                #     "json", product_stock_in_obj)
                data['product_stock_in'] = product_stock_in_obj

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
            # sales_obj = Sales.objects.all()
            # data['Response'] = 'Position registered successfully'
            # sales_s = serializers.serialize(
            #     "json", sales_obj)
            data['product solid'] = 'product solid successfully'

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


# Stock in details
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def viewing_stock_in_product(request):
    if request.method == 'GET':

        data = {}

        product_stck_in = ProductStockIn.objects.all()
        # data['Response'] = 'Position registered successfully'
        product_in_s = serializers.serialize(
            "json", product_stck_in)

        product_str = json.loads(product_in_s)
        if product_str:
            j = 0
            for product_ in product_str:

                user_id = product_['fields']['user']
                phone_type_id = product_['fields']['phone_type']
                brand_id = product_['fields']['brand']
                phone_model_id = product_['fields']['phone_model']
                color_id = product_['fields']['color']
                storage_id = product_['fields']['storage']

                user_str = serializers.serialize(
                    "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

                user_json = json.loads(user_str)

                if user_json:
                    product_str[j]['fields']['user'] = user_json[0]

                phone_type_str = serializers.serialize(
                    "json", PhoneType.objects.filter(id=phone_type_id))
                phone_type_json = json.loads(phone_type_str)
                if phone_type_json:
                    product_str[j]['fields']['phone_type'] = phone_type_json[0]

                brand_str = serializers.serialize(
                    "json", Brand.objects.filter(id=brand_id))
                brand_json = json.loads(brand_str)
                if brand_json:
                    product_str[j]['fields']['brand'] = brand_json[0]

                phone_model_str = serializers.serialize(
                    "json", PhoneModel.objects.filter(id=phone_model_id))
                phone_model_json = json.loads(phone_model_str)
                if phone_model_json:
                    product_str[j]['fields']['phone_model'] = phone_model_json[0]

                color_str = serializers.serialize(
                    "json", Color.objects.filter(id=color_id))
                color_json = json.loads(color_str)
                if color_json:
                    product_str[j]['fields']['color'] = color_json[0]

                storage_str = serializers.serialize(
                    "json", Storage.objects.filter(id=storage_id))
                storage_json = json.loads(storage_str)
                if storage_json:
                    product_str[j]['fields']['storage'] = storage_json[0]

                j = j+1

        data['product_stock_in_details'] = product_str

        return Response(data)


# Sales details
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_sales_details(request):
    if request.method == 'GET':

        data = {}

        sales_objs = Sales.objects.all()
        # data['Response'] = 'Position registered successfully'
        sales_s = serializers.serialize(
            "json", sales_objs)

        sales_str = json.loads(sales_s)
        if sales_str:
            j = 0
            for sales_ in sales_str:

                product_stock_in_id = sales_['fields']['product_stock_in']
                shop_id = sales_['fields']['shop']

                stk_in_str = serializers.serialize(
                    "json", ProductStockIn.objects.filter(id=product_stock_in_id))

                stk_in_json = json.loads(stk_in_str)

                if stk_in_json:
                    sales_str[j]['fields']['product_stock_in'] = stk_in_json[0]

                shop_str = serializers.serialize(
                    "json", Shop.objects.filter(id=shop_id))
                shop_json = json.loads(shop_str)
                if shop_json:
                    sales_str[j]['fields']['shop'] = shop_json[0]
                j = j+1

        data['sales_details'] = sales_str

        return Response(data)

# Stock to Shop details
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_stock_to_shop_dtls(request):
    if request.method == 'GET':

        data = {}

        stock_to_shop_objs = StockToShop.objects.all()

        stock_to_shop_s = serializers.serialize(
            "json", stock_to_shop_objs)

        stock_to_shop_str = json.loads(stock_to_shop_s)
        if stock_to_shop_str:
            j = 0
            for stock_to_shop_ in stock_to_shop_str:

                product_id = stock_to_shop_['fields']['product']
                shop_to_id = stock_to_shop_['fields']['shop_to']

                stk_to_shop_str = serializers.serialize(
                    "json", ProductStockIn.objects.filter(id=product_id))

                stk_to_shop_json = json.loads(stk_to_shop_str)

                if stk_to_shop_json:
                    stock_to_shop_str[j]['fields']['product'] = stk_to_shop_json[0]

                shop_to_str = serializers.serialize(
                    "json", Shop.objects.filter(id=shop_to_id))
                shop_to_json = json.loads(shop_to_str)
                if shop_to_json:
                    stock_to_shop_str[j]['fields']['shop_to'] = shop_to_json[0]
                j = j+1

        data['stock_to_shop_details'] = stock_to_shop_str

        return Response(data)


# another version of stock in details

# Sale Products details by brand and phone type
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_stock_in_details(request):
    if request.method == 'GET':

        data = {}
        products_type_count = []
        smartphone_brand_count = []
        usr = request.user
        today = date.today()

        # phones count by phone type
        products_by_phone_typ = ProductStockIn.objects.values('phone_type__id', 'phone_type__type_name', 'phone_type__id').annotate(
            no_prod=Count('id')).filter(stock_status='in')
        # phones count by Brand
        prds_by_brand_typ = ProductStockIn.objects.values('brand__brand_name', 'brand__phone_type', 'brand__id').annotate(
            no_prod=Count('id')).filter(stock_status='in')

        for product in products_by_phone_typ:
            obj = {}
            obj['phone_type_id'] = product['phone_type__id']
            obj['type name'] = product['phone_type__type_name']
            obj['count'] = product['no_prod']

            products_type_count.append(obj)

        for brand_ty in prds_by_brand_typ:

            obj1 = {}
            obj1['id'] = brand_ty['brand__id']
            obj1['brand'] = brand_ty['brand__brand_name']
            obj1['type'] = brand_ty['brand__phone_type']
            obj1['count'] = brand_ty['no_prod']
            smartphone_brand_count.append(obj1)

        data['product count by type'] = products_type_count
        data['product count by Brand'] = smartphone_brand_count

        return Response(data)


# stock in by Brand details
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_stock_in_by_brand(request):
    if request.method == 'POST':
        id = request.data['brand_id']

        data = {}
        products_count = []
        model_typ = ProductStockIn.objects.values('phone_model__model_name', 'phone_model__id').annotate(
            no_count=Count('id')).filter(brand_id=id, stock_status='in')

        for product in model_typ:
            obj = {}
            obj['model_id'] = product['phone_model__id']
            obj['name'] = product['phone_model__model_name']
            obj['count'] = product['no_count']
            products_count.append(obj)

        data['model count'] = products_count

        return Response(data)


# stock in  detail by model
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def stock_in_details_by_model(request):
    if request.method == 'POST':
        model_id = request.data['model_id']
        data = {}
        product_in_by_model = []

        shop_prd_dtls = ProductStockIn.objects.filter(
            phone_model=model_id, stock_status='in')

        product_in_s = serializers.serialize(
            "json", shop_prd_dtls)

        product_str = json.loads(product_in_s)
        if product_str:
            j = 0
            for product_ in product_str:

                product_stock_in

                phone_type_id = product_['fields']['phone_type']
                brand_id = product_['fields']['brand']
                phone_model_id = product_['fields']['phone_model']
                color_id = product_['fields']['color']
                storage_id = product_['fields']['storage']

                phone_type_str = serializers.serialize(
                    "json", PhoneType.objects.filter(id=phone_type_id))
                phone_type_json = json.loads(phone_type_str)
                if phone_type_json:
                    product_str[j]['fields']['phone_type'] = phone_type_json[0]

                brand_str = serializers.serialize(
                    "json", Brand.objects.filter(id=brand_id))
                brand_json = json.loads(brand_str)
                if brand_json:
                    product_str[j]['fields']['brand'] = brand_json[0]

                phone_model_str = serializers.serialize(
                    "json", PhoneModel.objects.filter(id=phone_model_id))
                phone_model_json = json.loads(phone_model_str)
                if phone_model_json:
                    product_str[j]['fields']['phone_model'] = phone_model_json[0]

                color_str = serializers.serialize(
                    "json", Color.objects.filter(id=color_id))
                color_json = json.loads(color_str)
                if color_json:
                    product_str[j]['fields']['color'] = color_json[0]

                storage_str = serializers.serialize(
                    "json", Storage.objects.filter(id=storage_id))
                storage_json = json.loads(storage_str)
                if storage_json:
                    product_str[j]['fields']['storage'] = storage_json[0]
                product_str[j]['fields'].pop('stock_status')
                product_str[j]['fields'].pop('stock_loc')
                product_str[j]['fields'].pop('timestamp_in')
                product_str[j]['fields'].pop('timestamp_out')
                product_str[j]['fields'].pop('user')

                j = j+1
        # product_in_by_model.append(product_str)
        data['model_details'] = product_str

        return Response(data)


# All product details
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_product_details(request):
    if request.method == 'GET':
        id = request.query_params['id']
        data = {}
        product_stck_in = ProductStockIn.objects.filter(phone_model_id=id)

        product_in_s = serializers.serialize(
            "json", product_stck_in)

        product_str = json.loads(product_in_s)
        if product_str:
            j = 0
            for product_ in product_str:

                user_id = product_['fields']['user']
                phone_type_id = product_['fields']['phone_type']
                brand_id = product_['fields']['brand']
                phone_model_id = product_['fields']['phone_model']
                color_id = product_['fields']['color']
                storage_id = product_['fields']['storage']

                user_str = serializers.serialize(
                    "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

                user_json = json.loads(user_str)

                if user_json:
                    product_str[j]['fields']['user'] = user_json[0]

                phone_type_str = serializers.serialize(
                    "json", PhoneType.objects.filter(id=phone_type_id))
                phone_type_json = json.loads(phone_type_str)
                if phone_type_json:
                    product_str[j]['fields']['phone_type'] = phone_type_json[0]

                brand_str = serializers.serialize(
                    "json", Brand.objects.filter(id=brand_id))
                brand_json = json.loads(brand_str)
                if brand_json:
                    product_str[j]['fields']['brand'] = brand_json[0]

                phone_model_str = serializers.serialize(
                    "json", PhoneModel.objects.filter(id=phone_model_id))
                phone_model_json = json.loads(phone_model_str)
                if phone_model_json:
                    product_str[j]['fields']['phone_model'] = phone_model_json[0]

                color_str = serializers.serialize(
                    "json", Color.objects.filter(id=color_id))
                color_json = json.loads(color_str)
                if color_json:
                    product_str[j]['fields']['color'] = color_json[0]

                storage_str = serializers.serialize(
                    "json", Storage.objects.filter(id=storage_id))
                storage_json = json.loads(storage_str)
                if storage_json:
                    product_str[j]['fields']['storage'] = storage_json[0]

                j = j+1

        data['product_stock_in_details'] = product_str

        return Response(data)


# stock movement to shop
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def move_stock_to_shop(request):
    if request.method == 'POST':
        product_list = []

        product_list = request.data['product_list']
        loc_from = request.data['location_from_id']
        loca_to = request.data['location_to_id']
        moved_by = request.data['moved_by']
        error_emei = []
        for imei in product_list:

            p_id = ProductStockIn.objects.filter(
                imei_no=imei, stock_status='in')

            if p_id.exists():

                # stock movement
                move_p = ShopToShop(product_stock_in=p_id[0], shop_from_id=loc_from,
                                    shop_to_id=loca_to, moved_by_id=moved_by)
                move_p.save()

                # save in shop product
                product_in = ShopProduct(
                    product_stock_in=p_id[0], shop_available_id=loca_to)
                product_in.save()

                # save in product status table
                product_status = ShopProductStatus(
                    product_stock_in=p_id[0], shop_reference_id=loca_to)
                product_status.save()

                product = ProductStockIn.objects.filter(
                    imei_no=imei, stock_status='in').update(stock_status='out', timestamp_out=datetime.now())
            else:
                error_emei.append(imei)

        data = {}
        if error_emei:
            data['product not in stock'] = error_emei
        else:
            data['message'] = 'products moved'

        return Response(data)


# Shop Products details
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_shop_product(request):
    if request.method == 'POST':

        data = {}
        shop_id = request.data['shop_id']
        products_type_count = []
        smartphone_brand_count = []
        usr = request.user
        positn = UserPositionAssignment.objects.filter(
            user=usr, assignment_status='Active')
        shp_assn = UserShopAssignment.objects.filter(
            user=usr, assignment_status='Active')

        # if positn:
        #     if positn[0].position.position_code == 'P006':
        #         # phones count by phone type
        #         products_by_phone_typ = ShopProduct.objects.values('shop_available__shop_name', 'product_stock_in__phone_type__type_name', 'product_stock_in__phone_type__id').annotate(
        #             no_prod=Count('product_stock_in')).filter(shop_available=shop_id, status='IN')
        #         # phones count by Brand
        #         prds_by_brand_typ = ShopProduct.objects.values('shop_available__shop_name', 'product_stock_in__brand__brand_name',
        #                                                        'product_stock_in__brand__id', 'product_stock_in__brand__phone_type__type_name').annotate(
        #             no_prod=Count('product_stock_in')).filter(shop_available=shop_id, status='IN')
        #     else:

        #         # phones count by phone type
        #         products_by_phone_typ = ShopProduct.objects.values('shop_available__shop_name', 'product_stock_in__phone_type__type_name', 'product_stock_in__phone_type__id').annotate(
        #             no_prod=Count('product_stock_in'))
        #         # phones count by Brand
        #         prds_by_brand_typ = ShopProduct.objects.values('shop_available__shop_name', 'product_stock_in__brand__brand_name',
        #                                                        'product_stock_in__brand__id', 'product_stock_in__brand__phone_type__type_name').annotate(no_prod=Count('product_stock_in'))
        products_by_phone_typ = ShopProduct.objects.values('shop_available__shop_name', 'shop_available__id', 'product_stock_in__phone_type__type_name', 'product_stock_in__phone_type__id').annotate(
            no_prod=Count('product_stock_in')).filter(shop_available_id=shop_id, status='IN')
        # phones count by Brand
        prds_by_brand_typ = ShopProduct.objects.values('shop_available__shop_name', 'product_stock_in__brand__brand_name',
                                                       'product_stock_in__brand__id', 'product_stock_in__brand__phone_type__type_name').annotate(
            no_prod=Count('product_stock_in')).filter(shop_available_id=shop_id, status='IN')
        for product in products_by_phone_typ:
            obj = {}
            obj['type name'] = product['product_stock_in__phone_type__type_name']
            obj['count'] = product['no_prod']
            obj['shop'] = product['shop_available__shop_name']
            obj['shop_id'] = product['shop_available__id']
            products_type_count.append(obj)

        for brand_ty in prds_by_brand_typ:

            obj1 = {}
            obj1['id'] = brand_ty['product_stock_in__brand__id']
            obj1['brand'] = brand_ty['product_stock_in__brand__brand_name']
            obj1['type'] = brand_ty['product_stock_in__brand__phone_type__type_name']
            obj1['count'] = brand_ty['no_prod']
            obj1['shop'] = product['shop_available__shop_name']
            obj1['shop_id'] = product['shop_available__id']

            smartphone_brand_count.append(obj1)

            data['product count by type'] = products_type_count
            data['product count by Brand'] = smartphone_brand_count
        # else:
        #     data['info'] = 'User not assigned any position'
        return Response(data)


# get stock from shop product table details by imei number
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def get_shop_product_by_imei(request):
    if request.method == 'POST':
        imei = request.data['imei_no']
        shop_id = request.data['shop_id']
        data = {}

        shop_product = ShopProduct.objects.filter(
            product_stock_in__imei_no=imei, shop_available_id=shop_id, status='IN')
        shop_p_s = ''
        product_str = 'product not in shop'
        if shop_product:
            prod = ProductStockIn.objects.filter(imei_no=imei)
            shop_p_s = serializers.serialize(
                "json", prod)
            product_str = json.loads(shop_p_s)
            if product_str:
                j = 0
                for product_ in product_str:

                    phone_type_id = product_['fields']['phone_type']
                    brand_id = product_['fields']['brand']
                    phone_model_id = product_['fields']['phone_model']
                    color_id = product_['fields']['color']
                    storage_id = product_['fields']['storage']

                    phone_type_str = serializers.serialize(
                        "json", PhoneType.objects.filter(id=phone_type_id))
                    phone_type_json = json.loads(phone_type_str)
                    if phone_type_json:
                        product_str[j]['fields']['phone_type'] = phone_type_json[0]

                    brand_str = serializers.serialize(
                        "json", Brand.objects.filter(id=brand_id))
                    brand_json = json.loads(brand_str)
                    if brand_json:
                        product_str[j]['fields']['brand'] = brand_json[0]

                    phone_model_str = serializers.serialize(
                        "json", PhoneModel.objects.filter(id=phone_model_id))
                    phone_model_json = json.loads(phone_model_str)
                    if phone_model_json:
                        product_str[j]['fields']['phone_model'] = phone_model_json[0]

                    color_str = serializers.serialize(
                        "json", Color.objects.filter(id=color_id))
                    color_json = json.loads(color_str)
                    if color_json:
                        product_str[j]['fields']['color'] = color_json[0]

                    storage_str = serializers.serialize(
                        "json", Storage.objects.filter(id=storage_id))
                    storage_json = json.loads(storage_str)
                    if storage_json:
                        product_str[j]['fields']['storage'] = storage_json[0]
                    product_str[j]['fields'].pop('stock_status')
                    product_str[j]['fields'].pop('stock_loc')
                    product_str[j]['fields'].pop('timestamp_in')
                    product_str[j]['fields'].pop('timestamp_out')
                    product_str[j]['fields'].pop('user')
                    j = j+1

        data['object'] = product_str

        return Response(data)


# receiving shop products
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def recieve_product_by_imei(request):
    if request.method == 'POST':
        imei = request.data['imei_no']
        shop_id = request.data['shop_id']
        data = {}

        shop_product = ShopProduct.objects.filter(
            product_stock_in__imei_no=imei, shop_available_id=shop_id, status='MVIN')
        if shop_product:
            ShopProduct.objects.filter(
                product_stock_in__imei_no=imei, shop_available_id=shop_id, status='MVIN').update(status='IN')

            product_id = shop_product[0].product_stock_in
            product_status = ShopProductStatus(
                product_stock_in=product_id, shop_status='IN', shop_reference_id=shop_id)
            product_status.save()
            data['response'] = 'product received'
        else:
            data['response'] = 'product not sent to this stock'

        return Response(data)

# receiving shop products
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def sale_product(request):
    if request.method == 'POST':
        imei = request.data['imei_no']
        shop_id = request.data['shop']
        discount = request.data['discount']
        # markup = request.data['markup']
        actual_selling_price = request.data['actual_selling_price']
        actual_selling_price = int(actual_selling_price)
        data = {}

        shop_product = ShopProduct.objects.filter(
            product_stock_in__imei_no=imei, shop_available__id=shop_id)
        if shop_product:
            for shop_p in shop_product:
                selling_price = shop_p.product_stock_in.selling_price
                if actual_selling_price > selling_price:
                    markup = actual_selling_price - selling_price

                else:
                    markup = 0
                if shop_p.status == 'IN':
                    sales = Sales(product_stock_in_id=shop_p.product_stock_in.id, shop_id=shop_id,
                                  discount=discount, markup=markup, actual_selling_price=actual_selling_price)
                    sales.save()

                    # save in the product status
                    product_id = shop_p.product_stock_in.id
                    product_status = ShopProductStatus(
                        product_stock_in_id=product_id, shop_status='SLD', shop_reference_id=shop_id)
                    product_status.save()

                    # update shop product
                    ShopProduct.objects.filter(
                        product_stock_in__id=product_id, shop_available_id=shop_id).update(status='SLD')
                    data['response'] = 'product solid'
                elif shop_p.status == 'SLD':
                    data['response'] = 'product already solid'
                else:
                    data['response'] = 'not in stock'
        else:
            data['response'] = 'product not in stock'

        return Response(data)


# product in by Brand details
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_shop_product_by_brand(request):
    if request.method == 'POST':
        id = request.data['brand_id']
        shop_id = request.data['shop_id']
        data = {}
        products_count = []
        model_typ = ShopProduct.objects.values('product_stock_in__phone_model__model_name', 'product_stock_in__phone_model__id').annotate(
            no_count=Count('product_stock_in__phone_model')).filter(product_stock_in__brand_id=id, shop_available_id=shop_id, status='IN')

        for product in model_typ:
            obj = {}
            obj['model_id'] = product['product_stock_in__phone_model__id']
            obj['name'] = product['product_stock_in__phone_model__model_name']
            obj['count'] = product['no_count']
            products_count.append(obj)

        data['model count'] = products_count

        return Response(data)


# shop product details for the certain model
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_shop_product_by_model(request):
    if request.method == 'POST':
        model_id = request.data['model_id']
        shop_id = request.data['shop_id']
        data = {}
        shop_products_by_model = []
        shop_prod_by_models = ShopProduct.objects.filter(
            shop_available_id=shop_id, product_stock_in__phone_model_id=model_id, status='IN')

        for shop_prod_by_model in shop_prod_by_models:

            prod_id = shop_prod_by_model.product_stock_in.id
            shop_prd_dtls = ProductStockIn.objects.filter(id=prod_id)

            product_in_s = serializers.serialize(
                "json", shop_prd_dtls)

            product_str = json.loads(product_in_s)
            if product_str:
                j = 0
                for product_ in product_str:

                    product_stock_in

                    phone_type_id = product_['fields']['phone_type']
                    brand_id = product_['fields']['brand']
                    phone_model_id = product_['fields']['phone_model']
                    color_id = product_['fields']['color']
                    storage_id = product_['fields']['storage']

                    phone_type_str = serializers.serialize(
                        "json", PhoneType.objects.filter(id=phone_type_id))
                    phone_type_json = json.loads(phone_type_str)
                    if phone_type_json:
                        product_str[j]['fields']['phone_type'] = phone_type_json[0]

                    brand_str = serializers.serialize(
                        "json", Brand.objects.filter(id=brand_id))
                    brand_json = json.loads(brand_str)
                    if brand_json:
                        product_str[j]['fields']['brand'] = brand_json[0]

                    phone_model_str = serializers.serialize(
                        "json", PhoneModel.objects.filter(id=phone_model_id))
                    phone_model_json = json.loads(phone_model_str)
                    if phone_model_json:
                        product_str[j]['fields']['phone_model'] = phone_model_json[0]

                    color_str = serializers.serialize(
                        "json", Color.objects.filter(id=color_id))
                    color_json = json.loads(color_str)
                    if color_json:
                        product_str[j]['fields']['color'] = color_json[0]

                    storage_str = serializers.serialize(
                        "json", Storage.objects.filter(id=storage_id))
                    storage_json = json.loads(storage_str)
                    if storage_json:
                        product_str[j]['fields']['storage'] = storage_json[0]
                    product_str[j]['fields'].pop('stock_status')
                    product_str[j]['fields'].pop('stock_loc')
                    product_str[j]['fields'].pop('timestamp_in')
                    product_str[j]['fields'].pop('timestamp_out')
                    product_str[j]['fields'].pop('user')
                    shop_products_by_model.append(product_str)
                    j = j+1

        data['product_stock_in_details'] = shop_products_by_model

        return Response(data)


# Sale Products details by brand and phone type
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_sale_product(request):
    if request.method == 'POST':

        data = {}
        products_type_count = []
        smartphone_brand_count = []
        usr = request.user
        today = date.today()
        shop_id = request.data['shop_id']

        # phones count by phone type
        products_by_phone_typ = Sales.objects.values('shop__shop_name', 'product_stock_in__phone_type__type_name', 'product_stock_in__phone_type__id').annotate(
            no_prod=Count('product_stock_in')).filter(shop_id=shop_id)
        # phones count by Brand
        prds_by_brand_typ = Sales.objects.values('shop__shop_name', 'shop__id', 'product_stock_in__brand__brand_name', 'product_stock_in__brand__id',
                                                 'product_stock_in__brand__phone_type__type_name').annotate(no_prod=Count('product_stock_in')).filter(shop_id=shop_id)

        for product in products_by_phone_typ:
            obj = {}
            obj['type name'] = product['product_stock_in__phone_type__type_name']
            obj['count'] = product['no_prod']
            obj['shop'] = product['shop__shop_name']

            products_type_count.append(obj)

        for brand_ty in prds_by_brand_typ:

            obj1 = {}
            obj1['id'] = brand_ty['product_stock_in__brand__id']
            obj1['brand'] = brand_ty['product_stock_in__brand__brand_name']
            obj1['type'] = brand_ty['product_stock_in__brand__phone_type__type_name']
            obj1['count'] = brand_ty['no_prod']
            obj1['shop'] = brand_ty['shop__shop_name']
            obj1['shop_id'] = brand_ty['shop__id']

            smartphone_brand_count.append(obj1)

        data['product count by type'] = products_type_count
        data['product count by Brand'] = smartphone_brand_count

        return Response(data)


# sales by Brand details
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_sales_by_brand(request):
    if request.method == 'POST':
        id = request.data['brand_id']
        shop_id = request.data['shop_id']
        data = {}
        products_count = []
        model_typ = Sales.objects.values('product_stock_in__phone_model__model_name', 'product_stock_in__phone_model__id').annotate(
            no_count=Count('product_stock_in__phone_model')).filter(product_stock_in__brand_id=id, shop_id=shop_id)

        for product in model_typ:
            obj = {}
            obj['model_id'] = product['product_stock_in__phone_model__id']
            obj['name'] = product['product_stock_in__phone_model__model_name']
            obj['count'] = product['no_count']
            products_count.append(obj)

        data['model count'] = products_count

        return Response(data)


# sales detail by model
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def sales_model_details(request):
    if request.method == 'POST':
        model_id = request.data['model_id']
        shop_id = request.data['shop_id']
        data = {}
        sale_products_by_model = []
        shop_prod_by_models = Sales.objects.filter(
            shop_id=shop_id, product_stock_in__phone_model_id=model_id)

        for shop_prod_by_model in shop_prod_by_models:

            prod_id = shop_prod_by_model.product_stock_in.id
            shop_prd_dtls = ProductStockIn.objects.filter(id=prod_id)

            product_in_s = serializers.serialize(
                "json", shop_prd_dtls)

            product_str = json.loads(product_in_s)
            if product_str:
                j = 0
                for product_ in product_str:

                    product_stock_in

                    phone_type_id = product_['fields']['phone_type']
                    brand_id = product_['fields']['brand']
                    phone_model_id = product_['fields']['phone_model']
                    color_id = product_['fields']['color']
                    storage_id = product_['fields']['storage']

                    phone_type_str = serializers.serialize(
                        "json", PhoneType.objects.filter(id=phone_type_id))
                    phone_type_json = json.loads(phone_type_str)
                    if phone_type_json:
                        product_str[j]['fields']['phone_type'] = phone_type_json[0]

                    brand_str = serializers.serialize(
                        "json", Brand.objects.filter(id=brand_id))
                    brand_json = json.loads(brand_str)
                    if brand_json:
                        product_str[j]['fields']['brand'] = brand_json[0]

                    phone_model_str = serializers.serialize(
                        "json", PhoneModel.objects.filter(id=phone_model_id))
                    phone_model_json = json.loads(phone_model_str)
                    if phone_model_json:
                        product_str[j]['fields']['phone_model'] = phone_model_json[0]

                    color_str = serializers.serialize(
                        "json", Color.objects.filter(id=color_id))
                    color_json = json.loads(color_str)
                    if color_json:
                        product_str[j]['fields']['color'] = color_json[0]

                    storage_str = serializers.serialize(
                        "json", Storage.objects.filter(id=storage_id))
                    storage_json = json.loads(storage_str)
                    if storage_json:
                        product_str[j]['fields']['storage'] = storage_json[0]
                    product_str[j]['fields'].pop('stock_status')
                    product_str[j]['fields'].pop('stock_loc')
                    product_str[j]['fields'].pop('timestamp_in')
                    product_str[j]['fields'].pop('timestamp_out')
                    product_str[j]['fields'].pop('user')
                    sale_products_by_model.append(product_str)
                    j = j+1

        data['sales_products_details'] = sale_products_by_model

        return Response(data)


# list of positions
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])viewing stock-in product
def get_list_details(request):
    if request.method == 'GET':
        id = request.query_params['id']
        data = {}
        product_stck_in = ProductStockIn.objects.filter(phone_model_id=id)

        product_in_s = serializers.serialize(
            "json", product_stck_in)

        product_str = json.loads(product_in_s)
        if product_str:
            j = 0
            for product_ in product_str:

                user_id = product_['fields']['user']
                phone_type_id = product_['fields']['phone_type']
                brand_id = product_['fields']['brand']
                phone_model_id = product_['fields']['phone_model']
                color_id = product_['fields']['color']
                storage_id = product_['fields']['storage']

                user_str = serializers.serialize(
                    "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

                user_json = json.loads(user_str)

                if user_json:
                    product_str[j]['fields']['user'] = user_json[0]

                phone_type_str = serializers.serialize(
                    "json", PhoneType.objects.filter(id=phone_type_id))
                phone_type_json = json.loads(phone_type_str)
                if phone_type_json:
                    product_str[j]['fields']['phone_type'] = phone_type_json[0]

                brand_str = serializers.serialize(
                    "json", Brand.objects.filter(id=brand_id))
                brand_json = json.loads(brand_str)
                if brand_json:
                    product_str[j]['fields']['brand'] = brand_json[0]

                phone_model_str = serializers.serialize(
                    "json", PhoneModel.objects.filter(id=phone_model_id))
                phone_model_json = json.loads(phone_model_str)
                if phone_model_json:
                    product_str[j]['fields']['phone_model'] = phone_model_json[0]

                color_str = serializers.serialize(
                    "json", Color.objects.filter(id=color_id))
                color_json = json.loads(color_str)
                if color_json:
                    product_str[j]['fields']['color'] = color_json[0]

                storage_str = serializers.serialize(
                    "json", Storage.objects.filter(id=storage_id))
                storage_json = json.loads(storage_str)
                if storage_json:
                    product_str[j]['fields']['storage'] = storage_json[0]

                j = j+1

        data['product_stock_in_details'] = product_str

        return Response(data)


