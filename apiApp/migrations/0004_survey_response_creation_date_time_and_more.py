# Generated by Django 4.0.3 on 2023-03-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0003_survey_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_response',
            name='creation_date_time',
            field=models.TextField(default='2023-03-10 18:23:24.671542+05:30'),
        ),
        migrations.AlterField(
            model_name='survey_templates',
            name='creation_date_time',
            field=models.TextField(default='2023-03-10 18:23:24.670544+05:30'),
        ),
        migrations.AlterField(
            model_name='user_surveys',
            name='creation_date_time',
            field=models.TextField(default='2023-03-10 18:23:24.670544+05:30'),
        ),
    ]
