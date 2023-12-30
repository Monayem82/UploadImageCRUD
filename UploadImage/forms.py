from django import forms
from django.forms import ModelForm,widgets
from .models import ImageStore

class ImageStoreForm(forms.ModelForm):
    class Meta:
        model=ImageStore
        fields="__all__"
    
    def __init__(self, *args, **kwargs):
        super(ImageStoreForm,self).__init__(*args, **kwargs)

        self.fields['image_name'].widget.attrs['class']='form-control'
        self.fields['image'].widget.attrs['class']='form-control'