from django.contrib.auth.models import User
from rest_framework import serializers
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django_api.settings.base import SOCIAL_GOOGLE_CLIENT_ID


class SocialLoginSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def verify_token(self, token):
        """
        Verify id_token is it right or not.
        :param token: JWT
        :return:
        """
        try:
            id_info = id_token.verify_oauth2_token(
                token, requests.Request(), SOCIAL_GOOGLE_CLIENT_ID)

            print(id_info)
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            if id_info['aud'] not in [SOCIAL_GOOGLE_CLIENT_ID]:
                raise ValueError('Could not verify audience.')

            # Success
            return id_info
        except ValueError:
            pass

    def create(self, validated_data):
        id_info = self.verify_token(validated_data.get("token"))
        if id_info:
            # User not exists
            # if not SocialAccount.objects.filter(unique_id=id_info["sub"]).exists():
            #     print("create user")
            # else:
            #     print("load user")
            # if not User.objects.filter(unique_id=id_info["sub"]).exists():
            #     print("")
            return User.objects.get(id=1)
        else:
            raise ValueError("Incorrect Credentials")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
