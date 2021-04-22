from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesSerializer


class EmployeesList(APIView):
    
    def get(self, request):
        serializer = EmployeesSerializer(Employees.objects.all(), many=True)
        return Response(serializer.data)
            
    def post(self, request):

        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)