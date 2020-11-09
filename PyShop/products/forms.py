from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from .models import ProductMain, SampleMultipleImgProduct, ProductMainImgs



class ProductMainAdminForm(forms.ModelForm):
    class Meta:
        model = ProductMain
        fields = ("name", "price", "description", "image_url", "stock", "gender", "categoryName")

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, productmain):
        for upload in self.files.getlist("photos"):
            photo = ProductMainImgs(show=productmain, photo=upload)
            photo.save()
