from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from adminstration.api.serializers import *
from django.core import serializers
import json
from rest_framework.renderers import JSONRenderer

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User
from adminstration.models import *


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_registration_api(request):
    if request.method == 'POST':
        serializer = ShopRegSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            position = serializer.save()
            data['Response'] = 'Position registered successfully'
            data['shop_name'] = position.shop_name

        else:
            data = serializer.errors
        return Response(data)


# Shop Update
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_update_api(request):
    if request.method == 'POST':
        # First getting the object id
        shop_id = request.data.get('id')
        data_from_post = request.data
        serializer = ShopRegSerializer(data=request.data)
        data = {}
        shop = Shop.objects.get(id=shop_id)
        shop_serializer = ShopRegSerializer(shop, data=data_from_post)

        if shop_serializer.is_valid():
            # validatedData = serializer.validated_data

            position = shop_serializer.save()
            data['Response'] = 'Position updated successfully'
            data['id'] = position.id

        else:
            data = serializer.errors
        return Response(data)


# Shop Assignment
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_assignment(request):
    if request.method == 'POST':
        serializer = ShopAssignmentSerializer(data=request.data)
        data = {}

        if serializer.is_valid():

            user = request.user

            shop = serializer.save(assigned_by=user)
            data['Response'] = 'Shop Assigned successfully'

        else:
            data = serializer.errors
        return Response(data)


# update shop assignment
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def shop_assignment_update(request):
    if request.method == 'POST':
        # First getting the object id
        obj_id = request.data.get('id')
        data_from_post = request.data
        # serializer = PositionAssignmentSerializer(data=request.data)
        data = {}
        shop_assign_obj = UserShopAssignment.objects.get(id=obj_id)
        user_shop_update_serializer = ShopAssignmentSerializer(
            shop_assign_obj, data=data_from_post)

        if user_shop_update_serializer.is_valid():
            # validatedData = serializer.validated_data

            updated_shop_assignment = user_shop_update_serializer.save()
            data['Response'] = 'User assignment updated successfully'

        else:
            data = user_shop_update_serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def position_assignment_api(request):
    if request.method == 'POST':
        serializer = PositionAssignmentSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            position = serializer.save()
            if position:
                User.objects.filter(id=position.user.id).update(
                    is_active=True, is_staff=True)
            data['Response'] = 'User assigned position successfully'
            data['user_id'] = position.user.id
        else:
            data = serializer.errors
        return Response(data)

# Update User Position Assignment api
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def user_assignment_update_api(request):
    if request.method == 'POST':
        # First getting the object id
        obj_id = request.data.get('id')
        data_from_post = request.data
        # serializer = PositionAssignmentSerializer(data=request.data)
        data = {}
        position_assign_obj = UserPositionAssignment.objects.get(id=obj_id)
        user_assignment_update_serializer = PositionAssignmentSerializer(
            position_assign_obj, data=data_from_post)

        if user_assignment_update_serializer.is_valid():
            # validatedData = serializer.validated_data

            updated_assignment = user_assignment_update_serializer.save()
            data['Response'] = 'User assignment updated successfully'
            data['id'] = updated_assignment.id

        else:
            data = user_assignment_update_serializer.errors
        return Response(data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def administration_api(request):
    if request.method == 'GET':
        shops = Shop.objects.all()
        shop_serializer = ShopRegSerializer(shops, many=True)

        serialized_all_users = serializers.serialize(
            "json", User.objects.all(), fields=('first_name', 'last_name', 'email'))
        serialized_all_users = json.loads(serialized_all_users)
        serialized_positions = serializers.serialize(
            "json", Position.objects.all())
        serialized_positions = json.loads(serialized_positions)
        shops_obj = serializers.serialize(
            "json", Shop.objects.all())
        shops_obj = json.loads(shops_obj)
        position_assigned = serializers.serialize(
            "json", UserPositionAssignment.objects.all())

        positions_asigned_json = json.loads(position_assigned)
        i = 0
        for position_asigned_json in positions_asigned_json:

            user_id = position_asigned_json['fields']['user']
            position_id = position_asigned_json['fields']['position']
            supervisor_id = position_asigned_json['fields']['supervisor']
            position_assigned_by = position_asigned_json['fields']['assigned_by']
            user_str = serializers.serialize(
                "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

            user_json = json.loads(user_str)
            # positions_asigned_json['fields']['user']
            if user_json:
                positions_asigned_json[i]['fields']['user'] = user_json[0]

            position_str = serializers.serialize(
                "json", Position.objects.filter(id=position_id))
            position_json = json.loads(position_str)
            if position_json:
                positions_asigned_json[i]['fields']['position'] = position_json[0]

            supervisor_str = serializers.serialize(
                "json", User.objects.filter(id=supervisor_id), fields=('first_name', 'last_name', 'email'))
            supervisor_json = json.loads(supervisor_str)
            if supervisor_json:
                positions_asigned_json[i]['fields']['supervisor'] = supervisor_json[0]

            position_assigned_by_str = serializers.serialize(
                "json", User.objects.filter(id=position_assigned_by), fields=('first_name', 'last_name', 'email'))
            position_assigned_json = json.loads(position_assigned_by_str)
            if position_assigned_json:
                positions_asigned_json[i]['fields']['assigned_by'] = position_assigned_json[0]

            i = i+1

        return Response({'all_users': serialized_all_users, 'all_positions': serialized_positions, 'all_shops': shops_obj, 'position_assignments': positions_asigned_json})
