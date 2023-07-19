from django import forms
from .models import Gallery


            
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title',  'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Painting'}),
            
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Painting'}),
        }