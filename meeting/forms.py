
from django import forms
from .models import Post

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["fileName", "image"]
    
