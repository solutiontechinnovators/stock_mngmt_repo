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
    path('position_list', views.position_list,
         name='position_list'),
    path('unassined_user_list', views.unassined_user_list,
         name='unassined_user_list'),
    path('assined_user_list', views.assined_user_list,
         name='assined_user_list'),
    path('shop_list', views.shop_list,
         name='shop_list'),
    path('user_without_shop', views.user_without_shop,
         name='user_without_shop'),
    path('shop_assigned_user_list', views.shop_assigned_user_list,
         name='shop_assigned_user_list'),
    path('position_re_assignment', views.position_re_assignment,
         name='position_re_assignment'),
     path('shop_re_assignment', views.shop_re_assignment,
         name='shop_re_assignment'),
]
