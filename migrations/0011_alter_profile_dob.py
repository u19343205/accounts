# Generated by Django 4.0.1 on 2022-01-28 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 15, 21, 20, 97534), verbose_name='date of birthd'),
        ),
    ]
