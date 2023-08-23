from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        access= refresh.access_token
        user_data= {
            'username':instance.username
        }
        access['user']=user_data
        data.update({
            'refresh': str(refresh),
            'access': str(access)
        })
        return data
    
class UserLoginSerializer(TokenObtainPairSerializer):
    username_field='username'