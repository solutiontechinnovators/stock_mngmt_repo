from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegSerializer
from django.core import serializers
import json

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
        user = serializers.serialize(
            "json", User.objects.all(), fields=('first_name'))
        # user = User.objects.filter(id=token.user_id)
        print(user)

        # return Response({'token': token.key, 'user_email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})
        return Response({'token': token.key, 'user': user})
