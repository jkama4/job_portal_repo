from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    """ A form for creating and updating Job instances. """
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'link', 'image']
