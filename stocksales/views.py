from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='login')
def save_product_stock_in(request):
    if request.method == "POST":
        product_in_form = ProductStockInForm(request.POST)
        if product_in_form.is_valid():

            product_in_form.save()
            return HttpResponse('Product entered')
    else:
        product_in_form = ProductStockInForm()
        # planning_strategic_goal_form.fields["strategic_goal_visible_status"].widget = forms.HiddenInput()
    return HttpResponse(product_in_form)
