from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configApp.models import Course
from configApp.serializers.teach_serializer import CourseSerializer

from rest_framework.views import APIView
from ..serializers import *


# fanlar uchun crud


class CourseApiView(ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    pagination_class = PageNumberPagination


# class TeacherViewApi(APIView):
#     def post(self,request):
#

class StudentViewApi(APIView):
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        students = Student.objects.all().order_by("-id")
        serializer = StudentGetSerializer(students, many=True)
        return Response(data=serializer.data)


class TeacherViewApi(ModelViewSet):
    queryset = Teacher.objects.all().order_by("-id")
    serializer_class = TableSerializer
