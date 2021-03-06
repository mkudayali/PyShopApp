# Generated by Django 3.1 on 2020-10-04 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employeePortal', '0010_timesheetdate_timesheetmain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetdate',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='timesheetmain',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='timesheetmain',
            name='title',
        ),
        migrations.AddField(
            model_name='timesheetdate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timesheetdate',
            name='hours',
            field=models.IntegerField(default=8),
        ),
        migrations.AddField(
            model_name='timesheetdate',
            name='instructions',
            field=models.TextField(blank=True),
        ),
    ]
