# Generated by Django 3.1 on 2020-08-23 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200823_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image1',
            new_name='Product Images',
        ),
    ]
