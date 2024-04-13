from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', CourseApiView)
router.register(r'room', RoomAPIView)
router.register(r'day', DayAPIView)
router.register(r'course', CourseApiView)
router.register(r'group', GroupApiView)
# dard javvali turi
router.register(r'tableType', TableTypeApi)
# dars jadvali
router.register(r'table', TableApi)
# yuqlama darajasini crud apilari
router.register(r'attendanceLevel', AttendanceLevelApi)
# yuqlama uchun crud
router.register(r'attendance', AttendanceApi)
router.register(r'region', RegionViewApi)
router.register(r'organization', OrganizationViewApi)
router.register(r'teacher', TeacherViewApi)
# o'qtuvchi tomonidan maczu qo'shish


urlpatterns = [
    path('', include(router.urls)),
    path('userRegister/', RegisterUserApi.as_view()),
    # path('userInfo/', UserInfo.as_view()),
    path('refresh_password/', ChangePasswordView.as_view()),
    path('studentApi/', StudentViewApi.as_view()),
]
