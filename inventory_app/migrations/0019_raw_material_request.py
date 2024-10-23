# Generated by Django 5.0.6 on 2024-10-23 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0018_finished_goods_request_stock'),
        ('purchase_app', '0003_rawmaterials_total_stock'),
        ('register_app', '0006_alter_department_dept_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raw_material_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(null=True)),
                ('input_date', models.DateField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(default='')),
                ('status', models.CharField(max_length=155, null=True)),
                ('response', models.TextField(default='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_app.rawmaterialcategory')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register_app.department')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_app.rawmaterials')),
            ],
        ),
    ]
