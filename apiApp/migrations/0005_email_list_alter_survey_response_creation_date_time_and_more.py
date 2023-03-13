# Generated by Django 4.0.3 on 2023-03-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0004_survey_response_creation_date_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('user_id', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='survey_response',
            name='creation_date_time',
            field=models.TextField(default='2023-03-13 14:18:53.503225+05:30'),
        ),
        migrations.AlterField(
            model_name='survey_templates',
            name='creation_date_time',
            field=models.TextField(default='2023-03-13 14:18:53.502227+05:30'),
        ),
        migrations.AlterField(
            model_name='user_surveys',
            name='creation_date_time',
            field=models.TextField(default='2023-03-13 14:18:53.503225+05:30'),
        ),
    ]
