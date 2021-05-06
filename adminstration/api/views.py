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
            data['Response'] = 'Shop registered successfully'
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
        obj_id = request.data.get('shop_assignment_id')
        data_from_post = request.data
        user = request.user
        data_from_post['assigned_by'] = user.id
        # serializer = PositionAssignmentSerializer(data=request.data)
        data = {}
        shop_assign_obj = UserShopAssignment.objects.get(id=obj_id)
        user_shop_update_serializer = ShopAssignmentSerializer(
            shop_assign_obj, data=data_from_post)

        if user_shop_update_serializer.is_valid():
            # validatedData = serializer.validated_data

            updated_shop_assignment = user_shop_update_serializer.save()
            data['Response'] = 'Shop assignment updated successfully'

        else:
            data = user_shop_update_serializer.errors
        return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def position_assignment_api(request):
    if request.method == 'POST':
        serializer = PositionAssignmentSerializer(data=request.data)
        data = {}
        logged_user = request.user
        if serializer.is_valid():
            position = serializer.save(assigned_by=logged_user)
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
        obj_id = request.data.get('assignment_id')
        data_from_post = request.data
        user = request.user
        data_from_post['assigned_by'] = user.id
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

        # populating id's with corresponding objects in position assigned
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

        # populating shops assigned ids with corresponding objects.
         # -----------------
        shops_assignment_obj = serializers.serialize(
            "json", UserShopAssignment.objects.all())
        shops_assignment_json_obj = json.loads(shops_assignment_obj)

        # ------------------
        j = 0
        for shop_assignment_json_obj in shops_assignment_json_obj:

            user_id = shop_assignment_json_obj['fields']['user']
            shop_id = shop_assignment_json_obj['fields']['shop']
            assigned_by_id = shop_assignment_json_obj['fields']['assigned_by']

            user_str = serializers.serialize(
                "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

            user_json = json.loads(user_str)

            if user_json:
                shops_assignment_json_obj[j]['fields']['user'] = user_json[0]

            shop_str = serializers.serialize(
                "json", Shop.objects.filter(id=shop_id))
            shop_json = json.loads(shop_str)
            if shop_json:
                shops_assignment_json_obj[j]['fields']['shop'] = shop_json[0]

            assigned_by_str = serializers.serialize(
                "json", User.objects.filter(id=assigned_by_id), fields=('first_name', 'last_name', 'email'))
            assigned_by_json = json.loads(assigned_by_str)
            if assigned_by_json:
                shops_assignment_json_obj[j]['fields']['assigned_by'] = assigned_by_json[0]

            j = j+1

        return Response({'all_users': serialized_all_users, 'all_positions': serialized_positions, 'all_shops': shops_obj, 'position_assignments': positions_asigned_json,
                         'shops_assignment_json_obj': shops_assignment_json_obj})


# deleting records
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def delete_shop(request):
    if request.method == 'POST':
        # First getting the object id
        obj_id = request.data.get('id')
        deleted_shop = Shop.objects.filter(id=obj_id).delete()
        print(deleted_shop)
        data = {}
        data['Response'] = 'Shop deleted successfully'
        return Response(data)

# retrieving all shop details
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_details(request):
    if request.method == 'GET':
        # First getting the object id
        shop_details = Shop.objects.all()
        shp_details = serializers.serialize(
            "json", shop_details)
        data = {}
        data['shop_details'] = shp_details

        return Response(data)

# retrieving all positions
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def position_list(request):
    if request.method == 'GET':
        # First getting the object id
        position_list = Position.objects.all()
        positn_list = serializers.serialize(
            "json", position_list, fields=('position_name', 'position_code'))
        data = {}
        data['position_list'] = positn_list

        return Response(data)

# retrieving all users without positions
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def unassined_user_list(request):
    if request.method == 'GET':
        # First getting the object id
        users = User.objects.all()
        unassingned_users = []
        for user in users:
            assigned_user = UserPositionAssignment.objects.filter(user=user)
            if assigned_user:
                pass
            else:
                unassingned_users.append(user)

        un_assigned_list = serializers.serialize(
            "json", unassingned_users, fields=('first_name', 'last_name', 'email'))
        print(len(unassingned_users))
        data = {}
        data['position_unassigned_user_list'] = un_assigned_list

        return Response(data)

# retrieving all users without positions
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def assined_user_list(request):
    if request.method == 'GET':
        # First getting the object id
        position_assigned = serializers.serialize(
            "json", UserPositionAssignment.objects.all())

        positions_asigned_json = json.loads(position_assigned)
        i = 0

        # populating id's with corresponding objects in position assigned
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

        return Response({'position_assignments': positions_asigned_json})

# retrieving all shops
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_list(request):
    if request.method == 'GET':
        # First getting the object id
        shops_list = Shop.objects.all()
        shop_list = serializers.serialize(
            "json", shops_list)
        data = {}
        data['shop_list'] = shop_list

        return Response(data)


# retrieving all users not assigned to shops
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def user_without_shop(request):
    if request.method == 'GET':
        # First getting the object id
        users = User.objects.all()
        unassingned_users = []
        for user in users:
            assigned_user = UserShopAssignment.objects.filter(user=user)
            if assigned_user:
                pass
            else:
                unassingned_users.append(user)

        un_assigned_list = serializers.serialize(
            "json", unassingned_users, fields=('first_name', 'last_name', 'email'))
        print(len(unassingned_users))
        data = {}
        data['shop_unassigned_user_list'] = un_assigned_list

        return Response(data)

# retrieving all users with shops assigned
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
# @authentication_classes([])
# @permission_classes([])
def shop_assigned_user_list(request):
    if request.method == 'GET':
        # First getting the object id
        shops_assignment_obj = serializers.serialize(
            "json", UserShopAssignment.objects.all())
        shops_assignment_json_obj = json.loads(shops_assignment_obj)

        # ------------------
        j = 0
        for shop_assignment_json_obj in shops_assignment_json_obj:

            user_id = shop_assignment_json_obj['fields']['user']
            shop_id = shop_assignment_json_obj['fields']['shop']
            assigned_by_id = shop_assignment_json_obj['fields']['assigned_by']
            shops_assignment_json_obj[j]['fields'].pop('timestamp')
            user_str = serializers.serialize(
                "json", User.objects.filter(id=user_id), fields=('first_name', 'last_name', 'email'))

            user_json = json.loads(user_str)

            if user_json:
                shops_assignment_json_obj[j]['fields']['user'] = user_json[0]

            shop_str = serializers.serialize(
                "json", Shop.objects.filter(id=shop_id))
            shop_json = json.loads(shop_str)
            if shop_json:
                shops_assignment_json_obj[j]['fields']['shop'] = shop_json[0]

            assigned_by_str = serializers.serialize(
                "json", User.objects.filter(id=assigned_by_id), fields=('first_name', 'last_name', 'email'))
            assigned_by_json = json.loads(assigned_by_str)
            if assigned_by_json:
                shops_assignment_json_obj[j]['fields']['assigned_by'] = assigned_by_json[0]

            j = j+1

        return Response({'shop_assignment_list': shops_assignment_json_obj})


# position re assignment
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def position_re_assignment(request):
    if request.method == 'POST':
        data_from_post = request.data

        user_id = data_from_post['user_id']
        position_id = data_from_post['position_id']
        user = request.user

        data = {}
        UserPositionAssignment.objects.filter(
            user_id = user_id, assignment_status='active').update(assignment_status='inactive')
        UserPositionAssignment(user_id = user_id, assignment_status='active', supervisor=user ,position_id=position_id, assigned_by=user).save()
        data = 're assigned successfully'
        return Response(data)


# shop re assignment
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def shop_re_assignment(request):
    if request.method == 'POST':
        data_from_post = request.data

        user_id = data_from_post['user_id']
        shop_id = data_from_post['shop_id']
        user = request.user

        data = {}
        UserShopAssignment.objects.filter(
            user_id = user_id, assignment_status='Active').update(assignment_status='Inactive')
        UserShopAssignment(user_id = user_id, assignment_status='Active',shop_id=shop_id, assigned_by=user).save()
        data = 're assigned successfully'
        return Response(data)

