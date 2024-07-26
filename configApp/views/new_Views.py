from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *


class FotosApi(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FotoSerializer
    queryset = NewsFotos.objects.all()

    pagination_class = PageNumberPagination


class NewsApi(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = PageNumberPagination


class NewsGetApi(APIView):
    # @swagger_auto_schema(request_body=NewsGETSerializer)
    def get(self, request):
        news = News.objects.all().order_by("-id")
        serializer = NewsGETSerializer(news, many=True)
        return Response(data=serializer.data)
