from django import forms
from . import models

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = models.ProfileImage
        fields = ["name", "image", "resized_image"]
