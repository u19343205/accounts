# Generated by Django 4.0.1 on 2022-02-01 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 11, 19, 56, 93785), verbose_name='date of birthd'),
        ),
    ]
