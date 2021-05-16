from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Employees, Users
from .serializers import EmployeesSerializer, UsersSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class EmployeesList(APIView):

    def get(self, request):
        serializer = EmployeesSerializer(Employees.objects.all(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name', 'last_name'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING)
        },
    ),
    )
    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
