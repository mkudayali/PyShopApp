# Generated by Django 3.1 on 2020-09-20 10:12

from django.db import migrations, models
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('employeePortal', '0006_auto_20200920_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheets',
            name='EmpUser',
            field=models.CharField(default=django_currentuser.middleware.get_current_authenticated_user, editable=None, max_length=100),
        ),
    ]
