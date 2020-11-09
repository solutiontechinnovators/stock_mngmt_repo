from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from adminstration.api.serializers import ShopRegSerializer, PositionAssignmentSerializer
from django.core import serializers
import json
from rest_framework.renderers import JSONRenderer

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User
from adminstration.models import Position, UserPositionAssignment, Shop, UserShopAssignment


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
