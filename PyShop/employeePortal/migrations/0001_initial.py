# Generated by Django 3.1 on 2020-09-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(max_length=255)),
                ('Description', models.TextField(default='', max_length=2048)),
                ('ContactName', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
                ('ContactNumber', models.CharField(max_length=12)),
                ('SpecialNotes', models.TextField(default='', max_length=2048)),
                ('Status', models.BooleanField()),
            ],
        ),
    ]
