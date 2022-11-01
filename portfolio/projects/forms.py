from django import forms
from .models import Project, comments


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['image'].widget.attrs['accept'] = '.png, .jpg, .jpeg'
    


