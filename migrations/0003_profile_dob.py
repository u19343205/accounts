# Generated by Django 4.0.1 on 2022-01-27 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_profile_course_profile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2022, 1, 27, 14, 41, 28, 346696), verbose_name='date of birthd'),
        ),
    ]
