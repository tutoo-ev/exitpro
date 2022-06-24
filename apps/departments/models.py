from django.db import models

# Create your models here.


class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    dept_code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f'{self.dept_code} - {self.dept_name}'

