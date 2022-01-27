# Generated by Django 4.0.1 on 2022-01-27 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0010_rename_module_id_assignment_module_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.TextField(default=models.CharField(choices=[('Assignment Related', 'Assignment Related'), ('Lecture Related', 'Lecture Related'), ('General', 'General')], default='General', max_length=20), max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 12, 30, 19, 353444), verbose_name='date published'),
        ),
    ]