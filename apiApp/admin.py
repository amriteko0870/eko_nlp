from django.contrib import admin
from apiApp.models import survey_templates
from apiApp.models import user_surveys
from apiApp.models import survey_response

# Register your models here.
admin.site.register(survey_templates)
admin.site.register(user_surveys)
admin.site.register(survey_response)