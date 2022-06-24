# from django.db import models
# from ..user.models import User
# from ..departments.models import Department
#
# # Create your models here.
#
#
# class AttritionDetail(models.Model):
#     class AttritionTypes(models.TextChoices):
#         VOLUNTARY = "VOLUNTARY", "Voluntary"
#         RESIGNATION = "RESIGNATION", "Resignation"
#         TERMINATION = "TERMINATION", "Termination"
#         DEATH = "DEATH", "Death"
#         RETIREMENT = "RETIREMENT", "Retirement"
#
#     employee = models.ForeignKey(User, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     effective_resignation_date = models.DateField()
#     attrition_type = models.CharField(choices=AttritionTypes.choices, default=AttritionTypes.VOLUNTARY)
#     reason_for_separation = models.CharField(max_length=200)
#     last_day_of_work = models.DateField()
#     date_of_hire = models.DateField()
#     resignation_letter = models.CharField(max_length=200)
#     rehire_eligibility = models.CharField(max_length=200)
#
#
