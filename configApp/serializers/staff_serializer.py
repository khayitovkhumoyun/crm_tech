from rest_framework import serializers

from . import UserSerializer
from ..models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "region", "title"]


class ManegerADDSerializer(serializers.Serializer):
    organization = serializers.IntegerField()
    phone = serializers.CharField(max_length=15)
    descriptions = serializers.CharField()


class ManagerOrgSerializer(serializers.Serializer):
    user = UserSerializer()
    organization = ManegerADDSerializer()


class ManagerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerOrganization
        fields = ["id", "user", "organization", "phone", "descriptions"]
