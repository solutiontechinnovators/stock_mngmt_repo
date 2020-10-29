from django.urls import path
from adminstration.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'adminstration'

urlpatterns = [
    path('position_registration', views.position_registration_api,
         name='position_registration'),
    path('position_assignment', views.position_assignment_api,
         name='position_assignment'),


]
