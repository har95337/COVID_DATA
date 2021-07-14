import datetime
from django.db import models
import django.utils

# Create your models here.
# data will be populated from /v3/covid-19/countries/USA
class Data(models.Model):
    total_deaths = models.IntegerField(default=0)
    active_cases = models.IntegerField(default=0)
    date_time = models.DateTimeField(blank = True)