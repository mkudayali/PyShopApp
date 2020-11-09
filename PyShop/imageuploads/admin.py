from .models import ImageUpload
from django.contrib import admin


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


#admin.site.register(ImageUpload, ImageUploadAdmin)
