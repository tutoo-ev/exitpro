from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DepartmentSerializer
from .models import Department

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    """Viewset manages Department"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

