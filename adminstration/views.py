from django.shortcuts import render
from adminstration.models import *
from adminstration.forms import *
from django.http import HttpResponse
from django import forms


# Create your views here.

def assign_user_position(request):
    # if request.method = 'POST':
    
    # else:
    user_assign_form  = UserPositionAssignmentForm()
    return render(request,'adminstration/assign_user_position.html',{'user_assign_form':user_assign_form})

def add_shop(request):
    # if request.method = 'POST':
    
    # else:
    add_shop_form  = ShopForm()
    return render(request,'adminstration/add_shop.html',{'add_shop_form':add_shop_form})

def assign_user_shop(request):
    # if request.method = 'POST':
    
    # else:
    shop_assign_form  = UserShopAssignmentForm()
    return render(request,'adminstration/assign_shop.html',{'shop_assign_form':shop_assign_form})

