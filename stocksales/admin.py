from django.contrib import admin
from .models import PhoneType, Brand, PhoneModel, Color, Storage, ProductStockIn, StockToShop, ShopToShop, ShopProduct, Sales

# Register your models here.


# class PositionAdmin(admin.ModelAdmin):
#     list_display = ['position_name', 'position_code']
#     # ordering = ['last_login']
#     list_per_page = 5  # No of records per page
#     list_filter = ('position_code',)


# class ShopAdmin(admin.ModelAdmin):
#     list_display = ['shop_name', 'shop_no', 'sector', 'district']
#     # ordering = ['last_login']
#     list_per_page = 5  # No of records per page
#     list_filter = ('shop_no',)


# class UserPositionAssignmentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'position',
#                     'assignment_status', 'supervisor', 'assigned_by']
#     # ordering = ['last_login']
#     list_per_page = 5  # No of records per page
#     list_filter = ('position',)


admin.site.register(PhoneType)
admin.site.register(Brand)
admin.site.register(PhoneModel)
admin.site.register(Color)
admin.site.register(Storage)
admin.site.register(ProductStockIn)
