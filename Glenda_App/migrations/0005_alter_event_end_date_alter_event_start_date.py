# Generated by Django 4.1.2 on 2024-10-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glenda_App', '0004_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(),
        ),
    ]