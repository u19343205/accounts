# Generated by Django 3.1.14 on 2022-01-21 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('duedate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('lead', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(choices=[('Assignment Related', 'Assignment Related'), ('Lecture Related', 'Lecture Related'), ('General', 'General')], default='General', max_length=20)),
                ('question', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='person',
        ),
        migrations.AddField(
            model_name='module',
            name='tutor',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='grade',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.module'),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.module'),
        ),
        migrations.RemoveField(
            model_name='module',
            name='year',
        ),
        migrations.AddField(
            model_name='grade',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.assignment'),
        ),
        migrations.AddField(
            model_name='module',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.course'),
        ),
    ]
