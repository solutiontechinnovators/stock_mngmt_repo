from django.shortcuts import render
from adminstration.models import *
from adminstration.forms import *
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth




# Create your views here.

def assign_user_position(request):
    user_assign_form = UserPositionAssignmentForm(request.POST)

    if user_assign_form.is_valid():

        instance = user_assign_form.save(commit=False)
        instance.assignment_status = 'active'
        instance.assigned_by = request.user 
        user_assign_form.save()
        # return redirect("/adminstration/assign_user_position")
        # messages.add_message(request, messages.INFO, '')
        messages.success(request, 'User has been assigned a position.')

      
    user_assign_form  = UserPositionAssignmentForm()
    return render(request,'adminstration/assign_user_position.html',{'user_assign_form':user_assign_form})

def add_shop(request):
    
    if request.method == 'POST':
        add_shop_form = ShopForm(request.POST)

        if add_shop_form.is_valid():
            add_shop_form.save()
            return redirect("/adminstration/add_shop")

    
    else:
        add_shop_form  = ShopForm()
        return render(request,'adminstration/add_shop.html',{'add_shop_form':add_shop_form})

def assign_user_shop(request):
    
    if request.method == 'POST':
        shop_assign_form = UserShopAssignmentForm(request.POST)

        if shop_assign_form.is_valid():

            instance = shop_assign_form.save(commit=False)
            instance.assignment_status = 'active'
            instance.assigned_by = request.user 
            shop_assign_form.save()
            return redirect("/adminstration/assign_user_shop")
    else:
        shop_assign_form  = UserShopAssignmentForm()
        return render(request,'adminstration/assign_shop.html',{'shop_assign_form':shop_assign_form})

def view_shops(request):
    
    
        return render(request,'adminstration/view_shops.html')

def view_assigned_shops(request):
    
    
        return render(request,'adminstration/view_assigned_shops.html')

def view_assigned_positions(request):
    
    
        return render(request,'adminstration/view_assigned_positions.html')



