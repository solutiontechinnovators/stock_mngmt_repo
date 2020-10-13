from rest_framework import serializers

from users.models import User


class UserRegSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'password', 'password2', ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'], email=self.validated_data['email'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must much. '})

        user.set_password(password)
        user.save()
        return user
