# Generated by Django 4.0.1 on 2022-01-27 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0015_alter_lecture_options_rename_course_id_module_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='module_id',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='question',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lecture',
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 15, 12, 56, 713030), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.TextField(default='WMGTSS Question', max_length=100),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
