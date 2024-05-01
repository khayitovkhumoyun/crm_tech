from rest_framework import serializers
from ..models import *


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'image', 'descriptions']


class ServesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serves
        fields = ['id', 'title']
