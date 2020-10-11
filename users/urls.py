from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up , name='sign_up'),



]