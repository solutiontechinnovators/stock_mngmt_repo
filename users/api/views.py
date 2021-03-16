from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegSerializer
from django.core import serializers
import json
from adminstration.models import Position, Shop, UserPositionAssignment, UserShopAssignment

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User


@api_view(['POST', ])
# @permission_classes((IsAuthenticated,))
@authentication_classes([])
@permission_classes([])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['Response'] = 'User registered successfully'
            data['email'] = user.email

        else:
            data = serializer.errors
        return Response(data)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        # user = serializers.serialize(
        #     "json", User.objects.all(), fields=('first_name'))
        user = User.objects.get(id=token.user_id)
        assigned_position = UserPositionAssignment.objects.filter(
            user_id=user.id, assignment_status='Active')

        
        shop_assigned = UserShopAssignment.objects.filter(
            user_id=user.id, assignment_status='Active')

        # if assigned_position:
        position_code = ''
        position_name = ''
        shop_id = ''
        shop_location = ''

        if assigned_position:
            position_code = assigned_position[0].position.position_code
            position_name = assigned_position[0].position.position_name

        if shop_assigned:
            shop = shop_assigned[0].shop
            shop_id = shop.id
            shop_location = shop.sector


        return Response({'token': token.key, 'user_email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'position_name': position_name, 'position_code': position_code, 'shop_id': shop_id, 'shop_location': shop_location})

        # return Response({'token': token.key, 'user': user})
