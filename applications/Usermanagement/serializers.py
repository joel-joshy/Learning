from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegistrationSeralizer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=60,min_length=6,write_only=True)


    class Meta:
        model = User
        fields = ['first_name','last_name','username','institution','email','password']

    def validate(self,attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')
        return attrs

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):

    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    username = serializers.CharField(min_length=3,read_only=True)
    tokens = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email','password','username','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user.is_active:
            raise AuthenticationFailed('Account disabled')
        if not user.is_verified:
            raise AuthenticationFailed('Account not verified')
        if not user:
            raise AuthenticationFailed('Invalid credentials!!')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }
        return super().validate(attrs)