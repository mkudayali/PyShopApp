# Generated by Django 3.1 on 2020-08-23 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200823_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoty_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.procategory', verbose_name='Category Name'),
        ),
    ]