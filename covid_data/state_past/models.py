from django.db import models

# Create your models here.
# data will be populated from https://disease.sh/v3/covid-19/nyt/states?lastdays=24
class Data(models.Model):
    state = models.CharField(max_length=50)
    past_total_cases: models.IntegerField(default=0)
    past_total_deaths: models.IntegerField(default=0)
    date_time = models.DateTimeField('date published')