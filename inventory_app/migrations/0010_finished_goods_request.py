# Generated by Django 5.0.6 on 2024-10-22 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0009_rename_edamaged_damaged_goods_stock_damaged'),
        ('production_app', '0008_damaged_goods_total_stock'),
        ('register_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finished_Goods_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('input_date', models.DateField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(default='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='production_app.water_finished_goods_category')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register_app.department')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='production_app.water_finished_goods')),
            ],
        ),
    ]