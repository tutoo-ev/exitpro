from django.contrib.auth.models import AbstractUser
from django.db import models
from ..departments.models import Department


class UserType(models.TextChoices):
    EMPLOYEE = "EMPLOYEE", "Employee"
    IT_SPECIALIST = "IT_SPECIALIST", "IT_Specialist"
    HR_MANAGER = "HR_MANAGER", "HR_Manager"
    SENIOR_BUSINESS_PARTNER = "SENIOR_BUSINESS_PARTNER", "Senior_Business_Partner"
    JUNIOR_BUSINESS_PARTNER = "JUNIOR_BUSINESS_PARTNER", "Junior_Business_Partner"
    RECRUITMENT_SUPERVISOR = "RECRUITMENT_SUPERVISOR", "Recruitment_Supervisor"
    SENIOR_PAYROLL_EXECUTIVE = "SENIOR_PAYROLL_EXECUTIVE", "Senior_Payroll_Executive"
    ADMIN = "ADMIN", "Admin"
    PARTNER = "PARTNER", "Partner"


class AttritionTypes(models.TextChoices):
    NA = "NOT_APPLICABLE", "Not_Applicable"
    VOLUNTARY = "VOLUNTARY", "Voluntary"
    RESIGNATION = "RESIGNATION", "Resignation"
    TERMINATION = "TERMINATION", "Termination"
    DEATH = "DEATH", "Death"
    RETIREMENT = "RETIREMENT", "Retirement"


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.EMPLOYEE)
    first_name = None
    last_name = None

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    effective_resignation_date = models.DateField(null=True, blank=True)
    attrition_type = models.CharField(max_length=60, choices=AttritionTypes.choices, default=AttritionTypes.NA,
                                      null=True, blank=True)
    reason_for_separation = models.CharField(max_length=200, null=True, blank=True)
    last_day_of_work = models.DateField(null=True, blank=True)
    date_of_hire = models.DateField(null=True, blank=True)
    resignation_letter = models.CharField(max_length=200, null=True, blank=True)
    rehire_eligibility = models.CharField(max_length=200, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='employees')
    # HR_MANAGER related fields
    bamboo_hr_active_status = models.BooleanField(default=True)
    nearest_payroll_salary_or_CA_on_hold = models.CharField(max_length=200, null=True, blank=True)
    clearance_and_exit_interview = models.CharField(max_length=200, null=True, blank=True)
    # instructions to ICT
    deactivate_door_badge = models.BooleanField(default=False)
    deactivate_biometric_access = models.BooleanField(default=False)
    deactivate_ev_mail = models.BooleanField(default=False)
    deactivate_pc_login = models.BooleanField(default=False)
    deactivate_client_tools_and_emails = models.BooleanField(default=False)
    company_assets_returned = models.BooleanField(default=False)
    # EVOX/Finance
    remove_from_evox_roster = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'mobile_number']

    class Meta:
        db_table = "user"

    def __str__(self):
        return f' {self.name} - {self.email}'


class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.EMPLOYEE)


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.ADMIN)


class HRManagerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.HR_MANAGER)


class PartnerUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.PARTNER)


class EmployeeUser(User):
    objects = EmployeeManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Employee"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.EMPLOYEE
        return super().save(*args, **kwargs)


class ITSpecialistManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.IT_SPECIALIST)


class ITSpecialistUser(User):
    objects = ITSpecialistManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "IT_Specialist"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.IT_SPECIALIST
        return super().save(*args, **kwargs)


class AdminUser(User):
    objects = AdminManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Admin"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.ADMIN
        return super().save(*args, **kwargs)


class HRManagerUser(User):
    objects = HRManagerManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "HR_MANAGER"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.HR_MANAGER
        return super().save(*args, **kwargs)


class PartnerUser(User):
    objects = PartnerUserManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "HR_MANAGER"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.PARTNER
        return super().save(*args, **kwargs)


class SeniorBusinessPartnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.SENIOR_BUSINESS_PARTNER)


class SeniorBusinessPartnerUser(User):
    objects = SeniorBusinessPartnerManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Senior_Business_Partner"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.SENIOR_BUSINESS_PARTNER
        return super().save(*args, **kwargs)


class JuniorBusinessPartnerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.JUNIOR_BUSINESS_PARTNER)


class JuniorBusinessPartnerUser(User):
    objects = JuniorBusinessPartnerManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Junior_Business_Partner"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.JUNIOR_BUSINESS_PARTNER
        return super().save(*args, **kwargs)


class RecruitmentSupervisorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.RECRUITMENT_SUPERVISOR)


class RecruitmentSupervisorUser(User):
    objects = RecruitmentSupervisorManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Recruitment_Supervisor"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.RECRUITMENT_SUPERVISOR
        return super().save(*args, **kwargs)


class SeniorPayrollExecutiveManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.SENIOR_PAYROLL_EXECUTIVE)


class SeniorPayrollExecutiveUser(User):
    objects = SeniorPayrollExecutiveManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Senior_Payroll_Executive"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserType.SENIOR_PAYROLL_EXECUTIVE
        return super().save(*args, **kwargs)


class EmployeeList(models.Model):
    user = models.ForeignKey(User, related_name='logged_user', on_delete=models.DO_NOTHING)
    employees = models.ForeignKey(User, related_name='employee_list', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Employee List under {self.user}"
