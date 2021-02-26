from django.urls import path
from adminstration.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'adminstration'

urlpatterns = [
    path('shop_registration', views.shop_registration_api,
         name='shop_registration'),
    path('position_assignment', views.position_assignment_api,
         name='position_assignment'),
    path('administration_api', views.administration_api,
         name='administration_api'),
    path('shop_update_api', views.shop_update_api,
         name='shop_update_api'),
    path('user_assignment_update_api', views.user_assignment_update_api,
         name='user_assignment_update_api'),
    path('shop_assignment', views.shop_assignment,
         name='shop_assignment'),
    path('shop_assignment_update', views.shop_assignment_update,
         name='shop_assignment_update'),
    path('delete_shop', views.delete_shop,
         name='delete_shop'),
    path('shop_details', views.shop_details,
         name='shop_details'),
]
