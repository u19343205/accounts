# Generated by Django 4.0.1 on 2022-01-27 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0013_alter_question_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 13, 33, 48, 112061), verbose_name='date published'),
        ),
    ]
