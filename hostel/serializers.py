from dataclasses import field
from functools import partial
from .models import *
from user.serializers import *
from rest_framework import serializers




class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostels
        fields ="__all__"
