import datetime

from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework.views import APIView
from ..models import *
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from ..serializers.mock_serializers import *


class StudentMonthMock(APIView):
    @swagger_auto_schema(request_body=StudentMock)
    def post(self, request):

        year = request.data["year"]

        if year is None:
            pass
        else:
            year = datetime.date.today().year

        students = Student.objects.filter(created__year=year).annotate(month=TruncMonth('created')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')
        student_data = {
            "data": students
        }
        return Response(data=student_data)


class DateToDateApi(APIView):
    @swagger_auto_schema(request_body=DateToDateStudentMock)
    def post(self, request):
        date1 = request.data['date1']
        date2 = request.data['date2']
        students = Student.objects.filter(created__gte=date1, created__lte=date2).annotate(
            month=TruncMonth('created')).values(
            'month').annotate(count=Count('id')).values(
            'month', 'count')
        student_data = {
            "data": students
        }
        return Response(data=student_data)


class CourseCountApi(APIView):
    def get(self, request):
        course = Course.objects.all().Count().order_by('-id')
        return Response(data={"count": course})
