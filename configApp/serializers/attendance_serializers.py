from ..models import *
from rest_framework import serializers


class AttendanceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLevel
        fields = ['id', 'title', 'descriptions']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["id", "level", "created",'student', "group"]
