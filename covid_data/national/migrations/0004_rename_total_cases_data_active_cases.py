# Generated by Django 3.2.5 on 2021-07-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('national', '0003_rename_cases_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='total_cases',
            new_name='active_cases',
        ),
    ]