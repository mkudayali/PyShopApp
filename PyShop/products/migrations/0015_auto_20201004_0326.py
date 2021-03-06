# Generated by Django 3.1 on 2020-10-04 08:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20201004_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmain',
            name='addedOn',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='ProductImgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.product')),
            ],
        ),
    ]
