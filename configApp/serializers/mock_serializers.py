from rest_framework import serializers


class StudentMock(serializers.Serializer):
    year = serializers.CharField(max_length=10)


class DateToDateStudentMock(serializers.Serializer):
    date1 = serializers.DateField()
    date2 = serializers.DateField()
