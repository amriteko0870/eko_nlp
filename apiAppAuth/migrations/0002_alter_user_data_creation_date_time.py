# Generated by Django 4.0.3 on 2023-03-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiAppAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='creation_date_time',
            field=models.TextField(default='2023-03-10 14:17:42.596591+05:30'),
        ),
    ]
