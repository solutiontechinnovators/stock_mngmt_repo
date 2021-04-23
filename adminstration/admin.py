from django.contrib import admin
from .models import Position, Shop, UserPositionAssignment, UserShopAssignment

# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ['position_name', 'position_code']
    # ordering = ['last_login']
    list_per_page = 5  # No of records per page
    list_filter = ('position_code',)


class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_no', 'sector', 'district']
    # ordering = ['last_login']
    list_per_page = 5  # No of records per page
    list_filter = ('shop_no',)


class UserPositionAssignmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'position',
                    'assignment_status', 'supervisor', 'assigned_by']
    # ordering = ['last_login']
    list_per_page = 5  # No of records per page
    list_filter = ('position',)


admin.site.register(Position,  PositionAdmin)
admin.site.register(Shop,  ShopAdmin)
admin.site.register(UserPositionAssignment, UserPositionAssignmentAdmin)
admin.site.register(UserShopAssignment)
