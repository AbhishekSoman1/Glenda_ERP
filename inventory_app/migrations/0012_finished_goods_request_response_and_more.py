# Generated by Django 5.0.6 on 2024-10-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0011_finished_goods_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='finished_goods_request',
            name='response',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='finished_goods_request',
            name='status',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
