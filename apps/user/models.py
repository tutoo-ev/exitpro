from django.contrib.auth.models import AbstractUser
from django.db import models
from ..departments.models import Department


class UserType(models.TextChoices):
    EMPLOYEE = "EMPLOYEE", "Employee"
    ADMIN = "ADMIN", "Admin"
    HR = "HR", "Hr"


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
    #HR related fields
    bamboo_hr_active_status = models.BooleanField(default=True)
    nearest_payroll_salary_or_CA_on_hold = models.CharField(max_length=200, null=True, blank=True)
    clearance_and_exit_interview = models.CharField(max_length=200, null=True, blank=True)
    #instructions to ICT
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


class HRManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=UserType.HR)


class EmployeeUser(User):
    objects = EmployeeManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "Employee"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.EMPLOYEE
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
            self.user_type = User.UserTypes.ADMIN
        return super().save(*args, **kwargs)


class HRUser(User):
    objects = HRManager()

    class Meta:
        proxy = True

    @staticmethod
    def get_user_type():
        return "HR"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = User.UserTypes.HR
        return super().save(*args, **kwargs)
