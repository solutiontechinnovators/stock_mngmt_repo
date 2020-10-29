from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from adminstration.api.serializers import ShopRegSerializer, PositionAssignmentSerializer
from django.core import serializers
import json

# testing login to return token and user details
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.models import User


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
