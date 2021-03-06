# Generated by Django 4.0.1 on 2022-02-02 12:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0030_alter_assignment_module_alter_question_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='curriculum.module'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 12, 35, 46, 774319), verbose_name='date published'),
        ),
    ]
