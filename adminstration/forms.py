from adminstration.models import *
from django import forms

class UserPositionAssignmentForm(forms.ModelForm):

    
    class Meta:
        model = UserPositionAssignment
        fields = (
                  "position",
                  "supervisor",
                  )

class ShopForm(forms.ModelForm):
    
    class Meta:
        model = UserPositionAssignment
        fields = (
                "user",
                "position",
                "supervisor",
                  )
class UserShopAssignmentForm(forms.ModelForm):

    class Meta:
        model = UserShopAssignment
        fields = (
                "user",
                "shop",
                    )



