from django.urls import path
from adminstration.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'adminstration'

urlpatterns = [
    path('shop_registration', views.shop_registration_api,
         name='shop_registration'),
    path('position_assignment', views.position_assignment_api,
         name='position_assignment'),


]
