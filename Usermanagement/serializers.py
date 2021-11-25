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
        # return super().validate(attrs)
    def create(self, validated_data):

        return User.objects.create_user(**validated_data)




class LoginSerializer(serializers.Serializer):



    email = serializers.EmailField()
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)
    tokens = serializers.CharField(read_only=True)

    # class Meta:
    #     model = User
    #     fields = ['email','password','tokens']
    #
    # def validate(self,attrs):
    #
    #     email = attrs.get('email','')
    #     password = attrs.get('password','')
    #     user = auth.authenticate(email=email,password=password)
    #     if not user:
    #         raise AuthenticationFailed('Invalid Credentials!!')
    #     if not user.is_active:
    #         raise AuthenticationFailed('Account disabled')
    #     if not user.is_verified:
    #         raise AuthenticationFailed('Account not verified')
    #
    #     return {
    #         'email':user.email,
    #         'tokens': user.tokens
    #     }

