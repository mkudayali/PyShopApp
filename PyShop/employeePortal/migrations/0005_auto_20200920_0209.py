# Generated by Django 3.1 on 2020-09-20 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeePortal', '0004_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='EndDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Timesheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('EmpUser', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
