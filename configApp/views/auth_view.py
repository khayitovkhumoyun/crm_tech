import requests
from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from ..serializers import *
from dotenv import load_dotenv

load_dotenv()

#

import random


# auth dan utgan user datelarini USER modelga saqlob quyadigan method
class RegisterUserApi(APIView):

    @swagger_auto_schema(request_body=UserSerializer)

    def post(self, request):
        print(self.request.user)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response({
                'status': True,
                'datail': 'Account create'
            })

    def get(self, request):
        users = User.objects.all().order_by('-id')
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)


# User passworni uzgartiradigan method
class ChangePasswordView(APIView):

    def patch(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(instance=self.request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserInfo(APIView):
#     @swagger_auto_schema(request_body=UserInfoSerializer)
#     def post(self, request):
#         username = request.data['username']
#         try:
#             user = User.objects.get(username=username)
#             if user.is_student == True:
#                 student = Student.objects.get(user__phone=phone)
#                 student_serializer = StudentSerializer(student)
#
#                 user_serializer = UserSerializer(user)
#                 data = {
#                     "user": student_serializer.data,
#                     "student": user_serializer.data
#                 }
#                 return Response(data=data)
#             elif user.is_staff == True:
#                 worker = Worker.objects.get(user__phone=phone)
#                 user_serializer = UserSerializer(user)
#                 worker_serializer = WorkerSerializer(worker)
#                 data = {
#                     "user": worker_serializer.data,
#                     "worker": user_serializer.data
#                 }
#                 return Response(data=data)
#             else:
#                 user_serializer = UserSerializer(user)
#
#                 return Response(data=user_serializer.data)
#         except Exception as e:
#             return Response(data={'error': f"{e}"})
