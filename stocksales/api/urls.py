from django.urls import path
from stocksales.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'adminstration'

urlpatterns = [
    path('reg_phone_type', views.reg_phone_type,
         name='reg_phone_type'),
    path('reg_brand', views.reg_brand,
         name='reg_brand'),
    path('reg_phone_model', views.reg_phone_model,
         name='reg_phone_model'),
    path('reg_color', views.reg_color,
         name='reg_color'),
    path('reg_storage', views.reg_storage,
         name='reg_storage'),
    path('product_stock_in', views.product_stock_in,
         name='product_stock_in'),
    path('shop_product', views.shop_product,
         name='shop_product'),
    path('sales_product', views.sales_product,
         name='sales_product'),
    path('stock_admin', views.stock_admin,
         name='stock_admin'),
    path('viewing_stock_in_product', views.viewing_stock_in_product,
         name='viewing_stock_in_product'),
    path('get_sales_details', views.get_sales_details,
         name='get_sales_details'),
    path('get_stock_to_shop_dtls', views.get_stock_to_shop_dtls,
         name='get_stock_to_shop_dtls'),
    path('get_stock_in_by_phone_type', views.get_stock_in_by_phone_type,
         name='get_stock_in_by_phone_type'),
    path('get_stock_in_by_model', views.get_stock_in_by_model,
         name='get_stock_in_by_model'),
    path('get_product_details', views.get_product_details,
         name='get_product_details'),
    path('move_stock_to_shop', views.move_stock_to_shop,
         name='move_stock_to_shop'),
    path('get_shop_product', views.get_shop_product,
         name='get_shop_product'),
]
