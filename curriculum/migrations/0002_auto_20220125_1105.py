# Generated by Django 3.1.14 on 2022-01-25 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 25, 11, 5, 4, 138236), verbose_name='date published'),
        ),
    ]