from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configApp.models import Course
from configApp.serializers.teach_serializer import CourseSerializer

from rest_framework.views import APIView
from ..serializers import *


# fanlar uchun crud


class CourseApiView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    pagination_class = PageNumberPagination


class StudentViewApi(APIView):
    permission_classes = [IsAuthenticated]

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


class StudentApiViewId(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentGetSerializer(student)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentGetSerializer(student, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def patch(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentGetSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})


class TeacherViewApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Teacher.objects.all().order_by("-id")
    serializer_class = TableSerializer
