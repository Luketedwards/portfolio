from django import forms
from .models import Project, comments
import datetime


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'image2','image3','image4','url', 'category', 'date', 'skills')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['image'].widget.attrs['accept'] = '.png, .jpg, .jpeg'
        self.fields['date'].widget.value = 23
    


