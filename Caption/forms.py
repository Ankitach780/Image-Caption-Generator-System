from django import forms
from .models import CaptionHistory

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = CaptionHistory
        fields = ['image']