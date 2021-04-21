from rest_framework import serializers
# from rest_framework import serializers.TokenSerializer
from adminstration.models import *
# from rest_auth.serializers import TokenSerializer
from django.contrib.auth import get_user_model


class ShopRegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['shop_name', 'shop_no',
                  'sector', 'district']


class ShopAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserShopAssignment
        fields = ['user', 'shop',
                  'assignment_status']


class PositionAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPositionAssignment
        fields = ['user', 'position',
                  'assignment_status', 'supervisor']
