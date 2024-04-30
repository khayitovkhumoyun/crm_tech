from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *


class RoomAPIView(ModelViewSet):
    queryset = Rooms.objects.all().order_by('-id')
    serializer_class = RoomSerializer
    pagination_class = PageNumberPagination


class DayAPIView(ModelViewSet):
    queryset = Day.objects.all().order_by('-id')
    serializer_class = DaySerializer
    pagination_class = PageNumberPagination


# group uchun crud
class GroupApiView(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer


class TableTypeApi(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = TableType.objects.all().order_by('-id')
    serializer_class = TableTypeSerializer


class TableApi(ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Table.objects.all().order_by('-id')
    serializer_class = TableSerializer


class GroupApi(APIView):
    pagination_class = PageNumberPagination

    # def get(self, request):
    #     teachers = Worker.objects.filter(user__is_teacher=True).order_by('-id')
    #     courses = Course.objects.all().order_by('-id')
    #     tables = Table.objects.all().order_by('-id')
    #     serializer_teachers = WorkerSerializer(teachers, many=True)
    #     serializer_courses = CourseSerializer(courses, many=True)
    #     serializer_table = TableSerializer(tables, many=True)
    #
    #     datas = {
    #         "teachers": serializer_teachers.data,
    #         "courses": serializer_courses.data,
    #         "tables": serializer_table.data
    #     }
    #
    #     return Response(data=datas)


# room id berilganda usha xonadadi bir kunlik qaysi guruhlarga dars bulsa shularni qaytaradi
class RoomTableApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        table_id = []
        table = Table.objects.filter(room=pk).order_by('-id')
        for item in table:
            table_id.append(item.id)
        groups = Group.objects.filter(table__id__in=table_id).order_by('-id')
        serializer = RoomTableSerializer(groups, many=True)
        return Response(data=serializer.data)


class GroupStudentsApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        students = Student.objects.filter(group__in=[pk])
        serializer_student = StudentSerializer(students, many=True)
        attendance = Attendance.objects.filter(group=pk).order_by('-id')
        serializer_attendance = AttendanceSerializer(attendance, many=True)
        data = {
            "student": serializer_student.data,
            "attendance": serializer_attendance.data
        }
        return Response(data=data)
