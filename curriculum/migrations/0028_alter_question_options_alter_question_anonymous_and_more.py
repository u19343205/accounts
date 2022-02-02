# Generated by Django 4.0.1 on 2022-02-02 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0027_question_anonymous_alter_question_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='question',
            name='anonymous',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Submit Anonymously'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 9, 32, 3, 781831), verbose_name='date published'),
        ),
    ]