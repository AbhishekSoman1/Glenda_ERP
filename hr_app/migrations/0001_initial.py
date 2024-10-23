# Generated by Django 4.1 on 2024-10-23 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(default='', max_length=120, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('emergency_contact_name', models.CharField(max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(max_length=15, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10, null=True)),
                ('salary_information', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('aadhar_no', models.CharField(max_length=12, null=True)),
                ('street', models.CharField(max_length=150, null=True)),
                ('pincode', models.CharField(max_length=9, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('landmark', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=120, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
