from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *


class AttendanceLevelApi(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = AttendanceLevel.objects.all().order_by('-id')
    serializer_class = AttendanceLevelSerializer


class AttendanceApi(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = AttendanceSerializer

