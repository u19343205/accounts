# Generated by Django 4.0.1 on 2022-01-27 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0016_remove_lecture_course_remove_lecture_module_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 15, 44, 20, 104700), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='curriculum.module'),
        ),
    ]
