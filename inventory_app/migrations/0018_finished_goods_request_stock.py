# Generated by Django 5.0.6 on 2024-10-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0017_remove_finished_goods_request_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='finished_goods_request',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]