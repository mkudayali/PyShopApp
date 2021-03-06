# Generated by Django 3.1 on 2020-10-04 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productmain_samplemultipleimgproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmain',
            name='category_name',
            field=models.CharField(choices=[('1', 'Bangles'), ('2', 'Bracelet'), ('3', 'Chains'), ('4', 'Ring'), ('5', 'Earring'), ('6', 'Mangalsutra'), ('7', 'Necklace'), ('8', 'Nosepin'), ('9', 'Pendant'), ('10', 'General')], default='Select Category', max_length=255),
        ),
        migrations.AddField(
            model_name='productmain',
            name='categoty_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.procategory', verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='productmain',
            name='description',
            field=models.TextField(default='', max_length=2048),
        ),
        migrations.AddField(
            model_name='productmain',
            name='image_url',
            field=models.CharField(blank=True, max_length=2083),
        ),
        migrations.AddField(
            model_name='productmain',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productmain',
            name='stock',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='samplemultipleimgproduct',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photoss', to='products.productmain'),
        ),
        migrations.CreateModel(
            name='ProductMainImgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.productmain')),
            ],
        ),
    ]
