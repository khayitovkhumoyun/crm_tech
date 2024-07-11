from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..serializers import *
from ..models import *
from rest_framework.response import Response


class RegionViewApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = RegionSerializer
    queryset = Region.objects.all().order_by('-id')
    pagination_class = PageNumberPagination


class GetRegionApi(APIView):
    def get(self, request):
        region = Region.objects.all().order_by('-id')
        serializer = RoomSerializer(region, many=True)

        return Response(data=serializer.data)


class OrganizationViewApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all().order_by('-id')
    pagination_class = PageNumberPagination


class GetOrganization(APIView):
    def get(self, request):
        org = Organization.objects.all().order_by('-id')
        serializer = OrganizationSerializer(org, many=True)
        return Response(data=serializer.data)


class ManagerApiView(APIView):
    @swagger_auto_schema(request_body=ManagerOrgSerializer)
    def post(self, request):
        try:
            user = request.data['user']
            user_serializer = UserSerializer(data=user)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
            organization = request.data['organization']
            organization["user"] = User.objects.get(username=user['username']).id
            manager_serializer = ManagerGetSerializer(data=organization)
            if manager_serializer.is_valid(raise_exception=True):
                manager_serializer.save()
                return Response({
                    'status': True,
                    'datail': 'Manager create'
                })
        except Exception as e:
            return Response(data={"error": e})

    def get(self, request):
        pagination_class = PageNumberPagination
        admins = ManagerOrganization.objects.filter(user__is_staff=True).order_by('-id')
        serializer = ManagerGetSerializer(instance=admins, many=True)
        return Response(data=serializer.data)


class ManagerApiIdView(APIView):
    def get(self, request, pk):
        try:
            worker = ManagerOrganization.objects.get(pk=pk)
            serializer = ManagerGetSerializer(worker)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def put(self, request, pk):
        try:
            teacher = ManagerOrganization.objects.get(id=pk)
            serializer = ManagerGetSerializer(teacher, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def patch(self, request, pk):
        try:
            teacher = ManagerOrganization.objects.get(pk=pk)
            serializer = ManagerGetSerializer(teacher, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})
