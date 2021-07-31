from django.contrib.auth.models import User
from rest_framework import serializers
from google.oauth2 import id_token
from google.auth.transport import requests

from django_api.settings import SOCIAL_GOOGLE_CLIENT_ID
from user.models import SocialAccount


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
