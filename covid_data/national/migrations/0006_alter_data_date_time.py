# Generated by Django 3.2.5 on 2021-07-14 16:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('national', '0005_alter_data_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 14, 16, 44, 21, 934091, tzinfo=utc)),
        ),
    ]
