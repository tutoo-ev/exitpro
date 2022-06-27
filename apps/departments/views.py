from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DepartmentSerializer
from .models import Department
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    """Viewset manages Department"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

