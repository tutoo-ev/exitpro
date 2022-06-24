from rest_framework.permissions import BasePermission
from .models import HRUser, AdminUser, EmployeeUser


class IsHR(BasePermission):
    def has_permission(self, request, view):
        user_available = HRUser.objects.filter(pk=request.user.pk).exists()
        print(user_available, "HR status")
        return user_available


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user_available = AdminUser.objects.filter(pk=request.user.pk).exists()
        print(user_available, "Admin status")
        return user_available


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        user_available = AdminUser.objects.filter(pk=request.user.pk).exists()
        print(user_available, "Employee user status")
        return user_available
