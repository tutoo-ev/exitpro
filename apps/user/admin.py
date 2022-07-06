from django.contrib import admin
from .models import User, EmployeeUser, EmployeeList, PartnerUser, ITSpecialistUser, SeniorBusinessPartnerUser, \
    SeniorPayrollExecutiveUser, JuniorBusinessPartnerUser, HRManagerUser
# Register your models here.

admin.site.register(User)
admin.site.register(EmployeeUser)
admin.site.register(EmployeeList)
admin.site.register(PartnerUser)
admin.site.register(ITSpecialistUser)
admin.site.register(SeniorBusinessPartnerUser)
admin.site.register(SeniorPayrollExecutiveUser)
admin.site.register(JuniorBusinessPartnerUser)
admin.site.register(HRManagerUser)

