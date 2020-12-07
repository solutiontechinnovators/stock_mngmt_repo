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
    path('stock_to_shop', views.stock_to_shop,
         name='stock_to_shop'),
    path('shop_to_shop', views.shop_to_shop,
         name='shop_to_shop'),
    path('shop_product', views.shop_product,
         name='shop_product'),
    path('sales_product', views.sales_product,
         name='sales_product'),
    path('stock_admin', views.stock_admin,
         name='stock_admin'),
]
