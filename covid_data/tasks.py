import requests
import json
import django.utils

import psycopg2

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

conn = psycopg2.connect(
    database="covid_db",
    user="postgres",
    password="covid",
    host="localhost",
    port="5432"
)

f = '%Y-%m-%d %H:%M:%S'

@shared_task
def getNationalData():
    SQL = "SELECT * FROM national_data;"
    cur = conn.cursor()
    cur.execute(SQL)
    return cur.fetchone()

@periodic_task(run_every=crontab(hour=7, minute=0))
def setNationalData():
    r = requests.get('https://disease.sh/v3/covid-19/countries/USA?strict=true')
    national_data = ''
    if r.status_code == 200:
        cur = conn.cursor()
        national_data = r.json()
        active_cases, total_deaths, date_time = national_data['active'], national_data['deaths'], django.utils.timezone.now(),
        cur.execute("DELETE FROM national_data;")
        SQL = "INSERT INTO national_data(active_cases, total_deaths, date_time) VALUES (%s, %s, %s);"
        data = (active_cases, total_deaths, date_time,)
        cur.execute(SQL, data)
        conn.commit()

@periodic_task(run_every=crontab(hour=7, minute=0))
def setStateData():
    r = requests.get('https://disease.sh/v3/covid-19/states')
    if r.status_code == 200:
        for state in r.json():
            cur = conn.cursor()
            name, active, total_deaths, recent_deaths, date_time = state['state'], state['active'], state['deaths'], state['todayDeaths'], django.utils.timezone.now()
            cur.execute("DELETE FROM state_data")
            SQL = "INSERT INTO state_data(state, active_cases, total_deaths, recent_deaths, date_time) VALUES (%s, %s, %s, %s, %s)"
            data = (name, active, total_deaths, recent_deaths, date_time)
            cur.execute(SQL, data)
        conn.commit()

@periodic_task(run_every=crontab(hour=7, minute=0))
def setPastStateData():
    r = requests.get('https://disease.sh/v3/covid-19/nyt/states?lastdays=24')
    if r.status_code == 200:
        state_data = r.json()
        N = len(state_data)
        for state in range(N - 56):
            cur = conn.cursor()
            name, past_total_cases, past_total_deaths, date_time = state['state'], state['cases'], state['deaths'], django.utils.timezone.now()
            cur.execute("DELETE * FROM state_data")
            SQL = "INSERT INTO state_data(state, active_cases, total_deaths, recent_deaths, date_time) VALUES (%s, %s, %s, %s)"
            data = (name, past_total_cases, past_total_deaths, date_time)
            cur.execute(SQL, data)
        conn.commit()