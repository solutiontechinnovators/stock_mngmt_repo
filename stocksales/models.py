from django.db import models
from users.models import User
from adminstration.models import *
# Create your models here.


class PhoneType(models.Model):

    type_name = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "phone_type" 

class Brand(models.Model):

    brand_name = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    phone = models.ForeignKey(PhoneType, on_delete=models.PROTECT)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = "brand" 

class PhoneModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.ForeignKey(PhoneType, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=60)
    processor = models.CharField(max_length=60)
    ram = models.CharField(max_length=60)
    camera_front = models.CharField(max_length=60)
    camera_back = models.CharField(max_length=60)
    screen_size = models.CharField(max_length=60)
    screen_resolution = models.CharField(max_length=60)
    battery_life = models.CharField(max_length=60)
    battery_type = models.CharField(max_length=60)
    operating_system = models.CharField(max_length=60)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = "phone_model"

class Color(models.Model):

    color_name = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.color_name

    class Meta:
        db_table = "color" 

class Storage(models.Model):

    storage_size = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.storage_size

    class Meta:
        db_table = "storage" 

class ProductStockIn(models.Model):

    user = models.ForeignKey(User , on_delete=models.PROTECT)
    phone = models.ForeignKey(PhoneType, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    phone_model = models.ForeignKey(PhoneModel, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    buying_price = models.CharField(max_length=60)
    selling_price = models.CharField(max_length=60)
    timestamp_in = models.DateField(auto_now_add=True)
    timestamp_out = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.timestamp_in

    class Meta:
        db_table = "product_stock_in"



class StockToShop(models.Model):

    product_stock_in = models.ForeignKey(ProductStockIn, on_delete=models.PROTECT)
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shop

    class Meta:
        db_table = "stock_to_shop" 

class ShopToShop(models.Model):

    product_stock_in = models.ForeignKey(ProductStockIn, on_delete=models.PROTECT)
    shop_from = models.ForeignKey(Shop,  related_name='shop_from',  on_delete=models.PROTECT)
    shop_to = models.ForeignKey(Shop, related_name='shop_to',  on_delete=models.PROTECT)

    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shop_from

    class Meta:
        db_table = "shop_to_shop" 

class ShopProduct(models.Model):

    product_stock_in = models.ForeignKey(ProductStockIn, on_delete=models.PROTECT)
    shop_available = models.ForeignKey(Shop,  on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shop_available

    class Meta:
        db_table = "shop_product" 

class Sales(models.Model):

    product_stock_in = models.ForeignKey(ProductStockIn, on_delete=models.PROTECT)
    shop = models.ForeignKey(Shop,  on_delete=models.PROTECT)
    discount = models.CharField(max_length=20)
    markup = models.CharField(max_length=20)
    actual_selling_price = models.CharField(max_length=20)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.actual_selling_price

    class Meta:
        db_table = "sales" 