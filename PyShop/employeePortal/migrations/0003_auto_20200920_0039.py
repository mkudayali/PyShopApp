# Generated by Django 3.1 on 2020-09-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeePortal', '0002_auto_20200920_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Description',
            field=models.TextField(blank=True, default='', max_length=2048),
        ),
        migrations.AlterField(
            model_name='projects',
            name='SpecialNotes',
            field=models.TextField(blank=True, default='', max_length=2048),
        ),
    ]
