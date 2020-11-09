from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.timezone import now

from django.db.models import Model
from django import forms
#from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    return "%s/%s" %(instance.id, filename)


class ProCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):

    itemCategoryChoices = (
            ('1', 'Bangles'),
            ('2', 'Bracelet'),
            ('3', 'Chains'),
            ('4', 'Ring'),
            ('5', 'Earring'),
            ('6', 'Mangalsutra'),
            ('7', 'Necklace'),
            ('8', 'Nosepin'),
            ('9', 'Pendant'),
            ('10', 'General')
    )

    itemGender = (
        ('1', 'Kids'),
        ('2', 'Men'),
        ('3', 'Women'),
        ('4', 'Unisex')
    )

    name = models.CharField(max_length=255)
    price = models.FloatField(blank=True)
    stock = models.IntegerField(blank=True)
    description = models.TextField(max_length=2048, default="")
    image_url = models.CharField(max_length=2083, blank=True)
    gender = models.CharField(max_length=10, default='Select Gender', choices=itemGender)
    category_name = models.CharField(max_length=255, default='Select Category', choices=itemCategoryChoices)
    product_images = models.ImageField(null=True,
                               blank=True,
                               upload_to=upload_location,
                               name="Product Images", default="")
    categoty_id = models.ForeignKey(ProCategory, default=0, verbose_name="Category Name", on_delete=models.SET_DEFAULT)


class ProductImgs(models.Model):
    show = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(blank=False)


class ProductMain(models.Model):
    itemCategoryChoices = (
            ('1', 'Bangles'),
            ('2', 'Bracelet'),
            ('3', 'Chains'),
            ('4', 'Ring'),
            ('5', 'Earring'),
            ('6', 'Mangalsutra'),
            ('7', 'Necklace'),
            ('8', 'Nosepin'),
            ('9', 'Pendant'),
            ('10', 'General')
    )

    itemGender = (
        ('1', 'Kids'),
        ('2', 'Men'),
        ('3', 'Women'),
        ('4', 'Unisex')
    )
    name = models.CharField(max_length=255)
    price = models.FloatField(blank=True, default=0)
    stock = models.IntegerField(blank=True, default=0)
    description = models.TextField(max_length=2048, default="")
    image_url = models.CharField(max_length=2083, blank=True)
    gender = models.CharField(max_length=10, default='Select Gender', choices=itemGender)
    category_name = models.CharField(max_length=255, default='Select Category', choices=itemCategoryChoices)
    addedOn = models.DateField(default=now)
    categoryName = models.ForeignKey(ProCategory, default=1, verbose_name="Category Name", on_delete=models.SET_DEFAULT)


class ProductMainImgs(models.Model):
    show = models.ForeignKey(
        ProductMain, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(blank=False)


class SampleMultipleImgProduct(models.Model):
    show = models.ForeignKey(
        ProductMain, on_delete=models.CASCADE, related_name="photoss"
    )
    photo = models.ImageField()
