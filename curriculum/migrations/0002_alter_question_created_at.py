# Generated by Django 4.0.1 on 2022-01-26 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 21, 37, 22, 475951), verbose_name='date published'),
        ),
    ]
