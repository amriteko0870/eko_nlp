import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random
import json
import PIL
from PIL import Image
from dotenv import load_dotenv

#-------------------------Django Modules---------------------------------------------
from django.http import Http404, HttpResponse, JsonResponse,FileResponse
from django.shortcuts import render
from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField
from django.db.models import F,Func,Q
from django.db.models import Value as V
from django.db.models.functions import Concat,Cast,Substr
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Min, Max
from django.db.models import Subquery
from django.core.files.storage import FileSystemStorage
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response

#------------------------------razorpay---------------------------------------------
import razorpay

# --------------------------- auth models ------------------------------------------
from apiAppAuth.models import user_data

# --------------------------- apiApp models ------------------------------------------
from apiApp.models import survey_templates
from apiApp.models import user_surveys
from apiApp.models import survey_response
from apiApp.models import email_list

#---------------------------- Extra -------------------------------------------------
from apiApp.email import sendEmailFunc