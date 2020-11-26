from adminstration.models import *
from django import forms

class UserPositionAssignmentForm(forms.ModelForm):

    
    class Meta:
        model = UserPositionAssignment
        fields = (
                    "user",
                    "position",
                    "supervisor",
                  )

class ShopForm(forms.ModelForm):
    
    class Meta:
        model = Shop
        fields = (
                "shop_name",
                "shop_no",
                "district",
                "sector",
                  )
class UserShopAssignmentForm(forms.ModelForm):

    class Meta:
        model = UserShopAssignment
        fields = (
                "user",
                "shop",
                    )



