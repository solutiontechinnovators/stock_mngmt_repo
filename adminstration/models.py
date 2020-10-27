from django.db import models
from users.models import User

# Create your models here.

# ***************Position Model***************


class Position(models.Model):
    position_name = models.CharField(max_length=100)
    position_code = models.CharField(max_length=20)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.position_name

    class Meta:
        db_table = "position"

# *******************USER_POSITION_ASSIGNMENT MODEL******************


class UserPositionAssignment(models.Model):
    user = models.ForeignKey(
        User, related_name='action_by', on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    assignment_status = models.CharField(max_length=20)
    supervisor = models.ForeignKey(
        User, related_name='supervisor', on_delete=models.PROTECT)
    assigned_by = models.ForeignKey(
        User, related_name='assigned_by', on_delete=models.PROTECT)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.assignment_status

    class Meta:
        db_table = "user_position_asignment"


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_no = models.IntegerField()
    sector = models.CharField(max_length=50)
    district = models.CharField(max_length=50)

    def __str__(self):
        return self.shop_name

    class Meta:
        db_table = "shop"


