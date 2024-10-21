from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Create your models here.
class department(models.Model):
    USER_TYPE_CHOICES = (
        ('Sales', 'Sales'),
        ('Purchase', 'Purchase'),
        ('Product', 'Product'),
        ('Logistics', 'Logistics'),
        ('Production', 'Production'),
        ('R & D', 'R & D'),
        ('HR', 'HR'),
    )
    dept_Name = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.dept_Name


class designation(models.Model):
    USER_TYPE_CHOICES = (
        ('CEO', 'CEO'),
        ('Manager', 'Manager'),
        ('Assistant Manager', 'Assistant Manager'),
        ('Executive', 'Executive'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    dept = models.ForeignKey(department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user_type} - {self.dept}"




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    designation = models.ForeignKey('designation', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('department', on_delete=models.SET_NULL, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Admin status
    is_superuser = models.BooleanField(default=False)  # Superuser status

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def _str_(self):
        return self.email


from django.db import models

class MenuPermissions(models.Model):
    user = models.ForeignKey('register_app.CustomUser', on_delete=models.CASCADE, null=True)  # Use the correct app name
    menu_details = models.ManyToManyField('Glenda_App.Menu', related_name='permissions')  # Use the correct app name

    def __str__(self):
        return ', '.join([menu.title for menu in self.menu_details.all()]) if self.menu_details.exists() else 'No Menu'

    class Meta:
        verbose_name = "Menu Permission"
        verbose_name_plural = "Menu Permissions"