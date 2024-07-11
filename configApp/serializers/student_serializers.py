from rest_framework import serializers

from . import UserSerializer
from ..models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'phone', 'group', 'organization', 'descriptions']


# GET UCHUN
class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name','is_activate', 'phone', 'group', 'organization', 'descriptions']
