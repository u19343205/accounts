# Generated by Django 4.0.1 on 2022-01-27 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0009_remove_question_subject_alter_question_assignment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='module_id',
            new_name='module',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='course',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 12, 23, 20, 458712), verbose_name='date published'),
        ),
    ]
