from rest_framework import serializers
from ..models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id', 'title', 'descriptions']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'title', 'descriptions']


class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = ['id', 'title', 'descriptions']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'start_time', 'end_time', 'room', 'type', 'descriptions']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'course', 'teacher', "table", 'start_date', 'end_date', 'price', 'descriptions']


class RoomTableSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        model = Group
        fields = ['id', 'title', 'course', 'teacher', "table", 'start_date', 'end_date', 'price', 'descriptions']
