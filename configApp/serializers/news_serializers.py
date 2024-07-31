from rest_framework import serializers
from ..models import *


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFotos
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'images', 'descriptions']


class NewsGETSerializer(serializers.ModelSerializer):
    images = FotoSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'images', 'descriptions']
