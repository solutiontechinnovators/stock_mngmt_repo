from django.contrib import admin

# Register your models here.
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_active','is_superuser','last_login']
    ordering = ['last_login']
    list_per_page = 5  # No of records per page
    list_filter = ('email',)


admin.site.register(User,  UserAdmin)
