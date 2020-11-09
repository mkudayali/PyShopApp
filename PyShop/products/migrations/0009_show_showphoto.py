# Generated by Django 3.1 on 2020-10-02 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200823_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('slug', models.SlugField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ShowPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='products.show')),
            ],
        ),
    ]