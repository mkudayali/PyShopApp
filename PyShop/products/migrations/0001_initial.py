# Generated by Django 3.1 on 2020-08-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('description', models.CharField(default='', max_length=2048)),
                ('image_url', models.CharField(max_length=2083)),
                ('gender', models.CharField(choices=[('1', 'Kids'), ('2', 'Men'), ('3', 'Women'), ('4', 'Unisex')], default='1', max_length=10)),
                ('category_name', models.CharField(choices=[('1', 'Bangles'), ('2', 'Bracelet'), ('3', 'Chains'), ('4', 'Ring'), ('5', 'Earring'), ('6', 'Mangalsutra'), ('7', 'Necklace'), ('8', 'Nosepin'), ('9', 'Pendant'), ('10', 'General')], default='1', max_length=255)),
                ('Image1', models.ImageField(default='', upload_to='')),
                ('Image2', models.ImageField(default='', upload_to='')),
                ('Image3', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
