
from django.contrib import auth

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    """
    serializer for user registration
    """

    password = serializers.CharField(max_length=60, min_length=6,
                                     write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'institution', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        return attrs

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    """
    serializer to verify email
    """
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    """
    serializer for login
    """
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=6,
                                     write_only=True)
    username = serializers.CharField(min_length=3, read_only=True)
    tokens = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials!!')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }


class LogoutSerializer(serializers.Serializer):

    """
    serializer to logout
    """
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ProfileDetailSerializer(serializers.ModelSerializer):
    """
    serializer for viewing profile
    """
    class Meta:

        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'mob_number', 'role', 'institution', 'employee_id',
            'is_active', 'is_verified'
        ]


class CompleteRegistrationSerializer(serializers.ModelSerializer):
    """
    serializer for registration completion
    """
    class Meta:

        model = User
        fields = ['mob_number', 'employee_id', 'institution']

        def validate(self, data):
            mob_number = data['mob_number']
            employee_id = data['employee_id']
            institution = data['institution']

            if not mob_number:
                raise serializers.ValidationError(
                    {
                        'status': False,
                        'error': {'errorMessage': "Enter mobile number"},
                        'data': {}

                    }
                )
            if not employee_id:
                raise serializers.ValidationError(
                    {
                        'status': False,
                        'error': {'errorMessage': "Enter employee ID"},
                        'data': {}

                    }
                )
            if not institution:
                raise serializers.ValidationError(
                    {
                        'status': False,
                        'error': {'errorMessage': "Enter Institution"},
                        'data': {}

                    }
                )
            return data
