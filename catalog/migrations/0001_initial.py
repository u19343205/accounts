# Generated by Django 3.1.14 on 2022-01-21 16:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('year', models.IntegerField()),
            ],
            options={
                'unique_together': {('id', 'name', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('modules', models.ManyToManyField(blank=True, to='catalog.Module')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.module')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.person')),
            ],
        ),
    ]
