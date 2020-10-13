from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from users.api.serializers import UserRegSerializer


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
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
