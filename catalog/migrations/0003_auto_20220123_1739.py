# Generated by Django 3.1.14 on 2022-01-23 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20220123_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 17, 39, 33, 968540), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
