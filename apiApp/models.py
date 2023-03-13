from datetime import datetime
import pytz
from django.db import models

# Create your models here.


class survey_templates(models.Model):
    survey = models.TextField(blank=True)
    config = models.TextField(blank=True)
    welcome_screen = models.TextField(blank=True)
    thank_you_screen = models.TextField(blank=True)
    survey_staus = models.BooleanField(default=True)
    creation_date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))

class user_surveys(models.Model):
    user_id = models.TextField()
    survey = models.TextField(blank=True)
    config = models.TextField(blank=True)
    welcome_screen = models.TextField(blank=True)
    thank_you_screen = models.TextField(blank=True)
    survey_staus = models.BooleanField(default=True)
    creation_date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))

class survey_response(models.Model):
    survey_id = models.TextField()
    survey = models.TextField()
    creation_date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))

class email_list(models.Model):
    email = models.TextField()
    user_id = models.TextField()