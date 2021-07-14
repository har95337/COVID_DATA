from django.db import models

# Create your models here.
# data will be populated from https://disease.sh/v3/covid-19/states
class Data(models.Model):
    state = models.CharField(max_length=50)
    active_cases: models.IntegerField(default=0)
    total_deaths: models.IntegerField(default=0)
    recent_deaths: models.IntegerField(default=0)
    date_time = models.DateTimeField()