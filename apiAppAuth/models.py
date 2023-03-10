from datetime import datetime
import pytz
from django.db import models

# Create your models here.

class user_data(models.Model):
    name = models.TextField()
    email = models.TextField()
    uid = models.TextField()
    creation_date_time = models.TextField(default=str(datetime.now(pytz.timezone("Asia/Kolkata"))))