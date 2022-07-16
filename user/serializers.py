from hostel.models import *
from .models import *
from hostel.serializers import HostelSerializer

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_owner'] = user.is_hostel
        return token


class HostelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelImages
        fields = "__all__"


class HostelRoomSerializer(serializers.ModelSerializer):
    hostel = HostelSerializer()
    class Meta:
        model = Rooms
        fields = "__all__"