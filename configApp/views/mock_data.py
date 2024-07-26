import datetime

from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from ..models import *
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from ..serializers.mock_serializers import *
from django.db.models import Count, Q


class StudentMonthMock(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course = Course.objects.all().Count().order_by('-id')
        return Response(data={"count": course})


class RegionsAndOrg(APIView):
    def get(self, request):
        regions = Region.objects.annotate(count=Count('organization')).values('id', 'title', 'count')
        context = {
            'regions': regions
        }
        return Response(data=context)


class OrgData(APIView):
    def get(self, request, pk):
        organization = Organization.objects.filter(region=pk).annotate(
            count_true=Count('student', filter=Q(student__is_activate=True)),
            count_false=Count('student', filter=Q(student__is_activate=False))).values('id',
                                                                                       'title',
                                                                                       'count_true', 'count_false')
        # print(organization)
        org = {"org": organization}

        return Response(data=org)
