# Generated by Django 4.0.1 on 2022-01-27 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2022, 1, 27, 15, 45, 55, 957052), verbose_name='date of birthd'),
        ),
    ]
