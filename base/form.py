from django.forms import ModelForm
from .models import imageUpload

class ImageUploadForm(ModelForm):
    class Meta:
        model = imageUpload
        fields = '__all__'