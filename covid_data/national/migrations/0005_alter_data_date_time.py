# Generated by Django 3.2.5 on 2021-07-14 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('national', '0004_rename_total_cases_data_active_cases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
