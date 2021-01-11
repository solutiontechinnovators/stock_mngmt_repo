from django import forms
from django.core.validators import FileExtensionValidator
from .models import *


class ProductStockInForm(forms.ModelForm):
    class Meta:
        model = ProductStockIn
        fields = ("imei_no",
                  "user",
                  "phone_type",
                  "brand",
                  "phone_model",
                  "color",
                  "storage",
                  "buying_price",
                  "selling_price")
