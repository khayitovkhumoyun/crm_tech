from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..serializers import *
from ..models import *


class RegionViewApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = RegionSerializer
    queryset = Region.objects.all().order_by('-id')
    pagination_class = PageNumberPagination


class OrganizationViewApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all().order_by('-id')
    pagination_class = PageNumberPagination

