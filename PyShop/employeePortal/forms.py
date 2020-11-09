from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from .models import TimeSheetMain, TimeSheetDate


class TimeSheetMainAdminForm(forms.ModelForm):
    class Meta:
        model = TimeSheetMain
        fields = (
            "SubmitDate",
        )

    #photos = forms.FileField(
    #       widget=forms.ClearableFileInput(attrs={"multiple": True}),
    #    label=_("Add photos"),
    #    required=False,
    #)

    #def clean_photos(self):
    #    for upload in self.files.getlist("photos"):
    #            validate_image_file_extension(upload)


    def save_photos(self, show):
        for upload in self.files.getlist("photos"):
            photo = TimeSheetDate(show=show, ProjectName = upload.ProjectName, date=upload.date, hours=upload.hours, instructions=upload.instructions, )
            photo.save()
