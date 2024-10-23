from django.db import models
from register_app.models import CustomUser
from django.contrib.auth.models import AbstractUser


class EmployeeDetails(models.Model):
    employee_id = models.CharField(max_length=120,null=True,default="")
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    joining_date = models.DateField(null=True)
    emergency_contact_name = models.CharField(max_length=100,null=True)
    emergency_contact_number = models.CharField(max_length=15,null=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],null=True)
    salary_information = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    aadhar_no = models.CharField(max_length=12,null=True)
    street = models.CharField(max_length=150,null=True)
    pincode = models.CharField(max_length=9,null=True)
    state = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    landmark = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=120,null=True)
    designation = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.user.name}-{self.designation}"
