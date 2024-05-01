from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *


class AboutApi(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = About.objects.all().order_by('-id')
    serializer_class = AttendanceSerializer


class AboutApiGet(APIView):
    def get(self, request):
        region = About.objects.all().order_by('-id')
        serializer = AttendanceSerializer(region, many=True)
        return Response(data=serializer.data)


class ServesApi(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Serves.objects.all().order_by('-id')
    serializer_class = ServesSerializer


class ServesApiGet(APIView):
    def get(self, request):
        region = Serves.objects.all().order_by('-id')
        serializer = ServesSerializer(region, many=True)
        return Response(data=serializer.data)
