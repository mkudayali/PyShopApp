from django.db import models

# Create your models here.


class ImageUpload(models.Model):
    name = models.CharField(max_length=150)
    image1 = models.ImageField(null=True,
                               blank=True, name="Image1", default="")

    def __str__(self):
        return self.name