# Generated by Django 4.0.1 on 2022-01-27 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0014_alter_question_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={},
        ),
        migrations.RenameField(
            model_name='module',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='course',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='position',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='module',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='question',
            name='standard',
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='curriculum.course'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='curriculum.course'),
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='curriculum.course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 14, 41, 28, 343527), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Standard',
        ),
    ]
